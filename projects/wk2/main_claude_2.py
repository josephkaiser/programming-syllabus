
'''
Repeated Number Guessing Game With Scoreboard

This program lets the player build win streaks by guessing numbers between 1-10.
players have 3 guesses per game. streaks unlock ranks on the global scoreboard.

adds a scoreboard.
undid my fix for the y/n play again bug. too easy to accidentally kill game with bad input.

date: november 3, 2025
'''
import random
import pyfiglet
import time
import json
import os
from datetime import datetime
from log_config import setup_logger

logger = setup_logger(__name__)

# Constants
MAX_GUESS_COUNT = 4
MIN_NUMBER = 1
MAX_NUMBER = 10
SCOREBOARD_FILE = "scoreboard.json"

RANKS = {
    0: "",
    1: "Winner",
    2: "Getting Started",
    4: "Here We Go",
    5: "Getting Into It",
    6: "Beginner",
    7: "Journeyperson",
    8: "Maestro",
    9: "Expert",
    10: "Ultimate",
    15: "Unparalleled",
    20: ":-)"
}

# ============================================================================
# SCOREBOARD FUNCTIONS
# ============================================================================

def load_scoreboard():
    """Load the scoreboard from JSON file."""
    if os.path.exists(SCOREBOARD_FILE):
        try:
            with open(SCOREBOARD_FILE, 'r') as f:
                data = json.load(f)
                logger.info("Scoreboard loaded successfully")
                return data
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Error loading scoreboard: {e}")
            return {"players": []}
    else:
        logger.info("No existing scoreboard found, creating new one")
        return {"players": []}


def save_scoreboard(scoreboard_data):
    """Save the scoreboard to JSON file."""
    try:
        with open(SCOREBOARD_FILE, 'w') as f:
            json.dump(scoreboard_data, f, indent=4)
        logger.info("Scoreboard saved successfully")
        return True
    except IOError as e:
        logger.error(f"Error saving scoreboard: {e}")
        return False


def add_score_entry(scoreboard_data, player_name, best_streak, total_games, total_wins, highest_rank):
    """Add or update a player's score in the scoreboard."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Check if player exists
    player_found = False
    for player in scoreboard_data["players"]:
        if player["name"].lower() == player_name.lower():
            player_found = True
            # Update if new best streak
            if best_streak > player["best_streak"]:
                player["best_streak"] = best_streak
                player["highest_rank"] = highest_rank if highest_rank else player.get("highest_rank", "None")
                player["last_played"] = timestamp
                logger.info(f"Updated {player_name}'s record with new best streak: {best_streak}")
            
            # Update cumulative stats
            player["total_games"] = player.get("total_games", 0) + total_games
            player["total_wins"] = player.get("total_wins", 0) + total_wins
            player["times_played"] = player.get("times_played", 0) + 1
            player["last_played"] = timestamp
            break
    
    # Add new player if not found
    if not player_found:
        new_entry = {
            "name": player_name,
            "best_streak": best_streak,
            "highest_rank": highest_rank if highest_rank else "None",
            "total_games": total_games,
            "total_wins": total_wins,
            "times_played": 1,
            "last_played": timestamp
        }
        scoreboard_data["players"].append(new_entry)
        logger.info(f"Added new player to scoreboard: {player_name}")
    
    return scoreboard_data


def get_sorted_scoreboard(scoreboard_data, sort_by="best_streak", limit=10):
    """Get sorted list of top players."""
    players = scoreboard_data.get("players", [])
    sorted_players = sorted(players, key=lambda x: x.get(sort_by, 0), reverse=True)
    return sorted_players[:limit]


def display_scoreboard(scoreboard_data, highlight_player=None):
    """Display the current scoreboard."""
    print("\n" + "=" * 80)
    print(pyfiglet.figlet_format("SCOREBOARD", width=80))
    print("=" * 80)
    
    players = get_sorted_scoreboard(scoreboard_data, sort_by="best_streak", limit=10)
    
    if not players:
        print("No scores yet. Be the first!")
        print("=" * 80 + "\n")
        return
    
    print(f"{'Rank':<6} {'Player':<20} {'Best Streak':<15} {'Highest Rank':<20} {'Win Rate':<10}")
    print("-" * 80)
    
    for idx, player in enumerate(players, 1):
        name = player["name"]
        best_streak = player["best_streak"]
        highest_rank = player.get("highest_rank", "None")
        total_games = player.get("total_games", 0)
        total_wins = player.get("total_wins", 0)
        
        # Calculate win rate
        win_rate = f"{(total_wins/total_games*100):.1f}%" if total_games > 0 else "N/A"
        
        # Highlight current player
        marker = ">>> " if highlight_player and name.lower() == highlight_player.lower() else ""
        
        print(f"{marker}{idx:<6} {name:<20} {best_streak:<15} {highest_rank:<20} {win_rate:<10}")
    
    print("=" * 80 + "\n")


def display_player_stats(scoreboard_data, player_name):
    """Display detailed stats for a specific player."""
    for player in scoreboard_data.get("players", []):
        if player["name"].lower() == player_name.lower():
            print("\n" + "=" * 60)
            print(f"STATS FOR {player_name.upper()}")
            print("=" * 60)
            print(f"Best Streak: {player['best_streak']}")
            print(f"Highest Rank: {player.get('highest_rank', 'None')}")
            print(f"Total Games Played: {player.get('total_games', 0)}")
            print(f"Total Wins: {player.get('total_wins', 0)}")
            print(f"Times Played: {player.get('times_played', 0)}")
            print(f"Last Played: {player.get('last_played', 'Unknown')}")
            
            total_games = player.get('total_games', 0)
            total_wins = player.get('total_wins', 0)
            if total_games > 0:
                win_rate = (total_wins / total_games) * 100
                print(f"Overall Win Rate: {win_rate:.1f}%")
            
            print("=" * 60 + "\n")
            return
    
    print(f"No stats found for {player_name}\n")


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def print_header():
    """Display the game title and instructions."""
    print(pyfiglet.figlet_format("Number Guessing Game"))
    print("Guess numbers between 1 and 10 in 3 tries or less.")
    print("Win consecutive games to build streaks and earn ranks!")
    print("Type 'q' at any time to quit.\n")


def print_game_start(game_number, current_streak):
    """Display the start of a new game with current streak info."""
    print("\n" + "=" * 60)
    print(f"GAME #{game_number} | Current Streak: {current_streak}")
    print("=" * 60)


def print_guess_prompt(guess_number):
    """Display the guess number in large text."""
    print(pyfiglet.figlet_format(f"Guess #{guess_number}"))


def print_feedback(player_name, rank_name, guess, target, is_correct):
    """Display feedback on the player's guess."""
    if is_correct:
        message = f"{rank_name} {player_name} guessed RIGHT!"
    elif guess > target:
        message = f"{rank_name} {player_name} guessed too HIGH!"
    else:
        message = f"{rank_name} {player_name} guessed too LOW!"
    
    print(pyfiglet.figlet_format(message))


def display_win(guess_count, streak):
    """Show celebration for winning a game."""
    print("\n" + " $ " * 30)
    print(pyfiglet.figlet_format(f"SUCCESS!"))
    print(f"You guessed correctly in {guess_count} guess{'es' if guess_count != 1 else ''}!")
    print(f"STREAK: {streak}")
    print(" $ " * 30 + "\n")
    time.sleep(1)


def display_streak_milestone(streak, rank_name):
    """Show special celebration when reaching a rank milestone."""
    print("\n" + "⭐" * 30)
    print(pyfiglet.figlet_format("RANK UP!"))
    print(f"You've reached a new rank: {rank_name.upper()}")
    print(f"Streak: {streak} wins")
    print("⭐" * 30 + "\n")
    time.sleep(2)


def display_loss(target_number, streak):
    """Show message when player runs out of guesses."""
    print("\n" + " L " * 30)
    print(f"Out of guesses! The number was {target_number}")
    if streak > 0:
        print(f"Your streak of {streak} has ended.")
    print(" L " * 30 + "\n")
    time.sleep(1)


def display_game_over(total_games, total_wins, total_guesses, highest_rank):
    """Show final statistics and game over screen."""
    print(pyfiglet.figlet_format("Game Over!"))
    print("\n" + "=" * 60)
    print("SESSION STATISTICS")
    print("=" * 60)
    print(f"Games Played This Session: {total_games}")
    print(f"Wins This Session: {total_wins}")
    print(f"Total Guesses Made: {total_guesses}")
    
    if total_wins > 0:
        avg_guesses = total_guesses / total_wins
        print(f"Average Guesses Per Win: {avg_guesses:.2f}")
    
    if highest_rank:
        print(f"Highest Rank Achieved: {highest_rank}")
    
    print("=" * 60 + "\n")


def display_new_record(player_name, new_streak):
    """Display celebration for a new personal best."""
    print("\n" + "🏆" * 30)
    print(pyfiglet.figlet_format("NEW RECORD!"))
    print(f"{player_name}, you've set a new personal best!")
    print(f"New Best Streak: {new_streak}")
    print("🏆" * 30 + "\n")
    time.sleep(2)


# ============================================================================
# INPUT FUNCTIONS
# ============================================================================

def get_player_name():
    """Get and validate the player's name."""
    logger.info("Getting player name")
    while True:
        name = input("What is your name, player?\n > ").strip().title()
        if name:
            logger.info(f"Player name: {name}")
            return name
        print("Please enter a valid name.")


def get_guess(guess_number):
    """Get and validate a guess from the player."""
    logger.info(f"Getting guess #{guess_number}")
    print_guess_prompt(guess_number)
    
    while True:
        user_input = input(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER} (or 'q' to quit): ").strip().lower()
        
        if user_input == 'q':
            return None
        
        try:
            guess = int(user_input)
            if MIN_NUMBER <= guess <= MAX_NUMBER:
                logger.info(f"Valid guess: {guess}")
                return guess
            else:
                print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")


# ============================================================================
# GAME LOGIC FUNCTIONS
# ============================================================================

def get_current_rank(streak):
    """Get the current rank name based on streak."""
    current_rank = None
    for threshold in sorted(RANKS.keys(), reverse=True):
        if streak >= threshold:
            current_rank = RANKS[threshold]
            break
    return current_rank


def check_rank_milestone(old_streak, new_streak):
    """Check if player reached a new rank milestone."""
    old_rank = get_current_rank(old_streak)
    new_rank = get_current_rank(new_streak)
    
    # Check if we crossed a threshold
    for threshold in sorted(RANKS.keys()):
        if old_streak < threshold <= new_streak:
            return True, RANKS[threshold]
    
    return False, None


def play_single_game(player_name, rank_name, game_number, current_streak):
    """
    Play a single round of the guessing game.
    
    Returns:
        tuple: (won: bool, guess_count: int, quit: bool, target_number: int)
    """
    logger.info(f"Beginning Game #{game_number}")
    print_game_start(game_number, current_streak)
    
    target_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    logger.info(f"Target number: {target_number}")
    
    for guess_count in range(1, MAX_GUESS_COUNT + 1):
        guess = get_guess(guess_count)
        
        # Player quit
        if guess is None:
            logger.info("Player chose to quit")
            return False, guess_count - 1, True, target_number
        
        # Check if correct
        if guess == target_number:
            print_feedback(player_name, rank_name, guess, target_number, is_correct=True)
            logger.info(f"Player won in {guess_count} guesses")
            return True, guess_count, False, target_number
        
        # Give feedback
        print_feedback(player_name, rank_name, guess, target_number, is_correct=False)
    
    # Out of guesses
    logger.info("Player lost - out of guesses")
    return False, MAX_GUESS_COUNT, False, target_number


def get_player_record(scoreboard_data, player_name):
    """Get a player's best streak from the scoreboard."""
    for player in scoreboard_data.get("players", []):
        if player["name"].lower() == player_name.lower():
            return player.get("best_streak", 0)
    return 0

# ============================================================================
# MAIN GAME LOOP
# ============================================================================

def main():
    """Main game loop managing streaks and statistics."""
    logger.info("Application started")
    print_header()
    scoreboard_data = load_scoreboard()
    display_scoreboard(scoreboard_data)
    
    player_name = get_player_name()

    
    # Get player's previous record
    previous_best = get_player_record(scoreboard_data, player_name)
    if previous_best > 0:
        print(f"\nWelcome back, {player_name}! Your best streak is {previous_best}.")
        display_player_stats(scoreboard_data, player_name)
    else:
        print(f"\nWelcome, {player_name}! Good luck in your first game.")
    
    # Game statistics
    current_streak = 0
    best_streak = 0
    total_games = 0
    total_wins = 0
    total_guesses = 0
    highest_rank = None
    new_record_set = False
    
    # Main game loop
    while True:
        total_games += 1
        
        rank_name = get_current_rank(current_streak)
        # Play a single game
        won, guess_count, player_quit, target_number = play_single_game(player_name, rank_name, total_games, current_streak)
        
        # Handle quit
        if player_quit:
            break
        
        total_guesses += guess_count
        
        # Handle win
        if won:
            total_wins += 1
            old_streak = current_streak
            current_streak += 1
            best_streak = max(best_streak, current_streak)
            
            display_win(guess_count, current_streak)
            
            # Check for new personal record
            if current_streak > previous_best:
                display_new_record(player_name, current_streak)
                new_record_set = True
            
            # Check for rank milestone
            reached_milestone, rank_name = check_rank_milestone(old_streak, current_streak)
            if reached_milestone:
                display_streak_milestone(current_streak, rank_name)
                highest_rank = rank_name
        
        # Handle loss
        else:
            display_loss(target_number, current_streak)
            
            # Reset streak
            if current_streak > 0:
                print(f"Streak ended at {current_streak}. Starting fresh!\n")
                current_streak = 0
        
        # Ask if player wants to continue
        while True:
            continue_game = input("Play another game? (y/n): ").strip().lower()
            if continue_game == 'y':
                break
            if continue_game == 'n':
                break
        if continue_game == 'n':
            break
    
    # Display final statistics
    if not highest_rank and best_streak > 0:
        highest_rank = get_current_rank(best_streak)
    
    display_game_over(total_games, total_wins, total_guesses, highest_rank)
    
    # Update scoreboard
    if best_streak > 0:
        scoreboard_data = add_score_entry(
            scoreboard_data, 
            player_name, 
            best_streak, 
            total_games, 
            total_wins, 
            highest_rank
        )
        
        if save_scoreboard(scoreboard_data):
            print("✓ Your score has been saved to the scoreboard!\n")
            
            # Show updated scoreboard
            display_scoreboard(scoreboard_data, highlight_player=player_name)
        else:
            print("✗ Error saving score to scoreboard.\n")
    
    logger.info(f"Application finished. Games: {total_games}, Wins: {total_wins}, Best Streak: {best_streak}")


if __name__ == "__main__":
    main()
