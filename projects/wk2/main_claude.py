'''
Repeated Number Guessing Game
This program lets the player build win streaks by guessing numbers between 1-10.
Players have 3 guesses per game. Streaks unlock ranks on the global scoreboard.

Revised code based on claude output. It separated my twisted logic into many different functions. These are as follows:
    print_header()
    print_game_start()
    print_guess_prompt()
    print_feedback()
    display_win()
    display_loss()
    display_streak_milestone()
    display_game_over()
    get_guess()
    get_player_name()
    get_current_rank()
    check_rank_milestone()
    play_single_game()

The revised main() function incorporates more detailed game logic, showing the transition from stage to stage and managing the display and score sequencing between rounds of game play.

I had the concept of display win, loss, streak, game over in my sketch of code but failed to implement with consistent function encapsulation.

Date: November 3, 2025
'''
import random
import pyfiglet
import time
from log_config import setup_logger

logger = setup_logger(__name__)

# Constants
MAX_GUESS_COUNT = 3
MIN_NUMBER = 1
MAX_NUMBER = 4

RANKS = {
    1: "Winner",
    2: "Getting Started",
    4: "Here We Go",
    5: "Getting Into It",
    6: "Beginner",
    7: "Journeyman",
    8: "Master",
    9: "Expert",
    10: "Ultimate",
    15: "Unparalleled",
    20: ":-) "
}


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


def print_feedback(player_name, guess, target, is_correct):
    """Display feedback on the player's guess."""
    if is_correct:
        message = f"{player_name} is CORRECT!"
    elif guess > target:
        message = f"{player_name} too HIGH!"
    else:
        message = f"{player_name} too LOW!"
    
    print(pyfiglet.figlet_format(message))


def display_win(guess_count, streak):
    """Show celebration for winning a game."""
    print("\n" + "_" * 30)
    print(f"SUCCESS! You guessed correctly in {guess_count} guess{'es' if guess_count != 1 else ''}!")
    print(f"STREAK: {streak}")
    print("_" * 30 + "\n")
    time.sleep(1)


def display_streak_milestone(streak, rank_name):
    """Show special celebration when reaching a rank milestone."""
    print("\n" + "⭐" * 30)
    print(pyfiglet.figlet_format("RANK UP!"))
    print(f"You've reached: {rank_name.upper()}")
    print(f"Streak: {streak} wins")
    print("⭐" * 30 + "\n")
    time.sleep(1)


def display_loss(target_number, streak):
    """Show message when player runs out of guesses."""
    print("\n" + "L" * 30)
    print(f"Loser! Out of guesses! The number was {target_number}")
    print(f"Your streak of {streak} has ended.")
    print("L" * 30 + "\n")
    time.sleep(1)


def display_game_over(total_games, total_wins, total_guesses, highest_rank):
    """Show final statistics and game over screen."""
    print(pyfiglet.figlet_format("Game Over!"))
    print("\n" + "=" * 60)
    print("FINAL STATISTICS")
    print("=" * 60)
    print(f"Total Games Played: {total_games}")
    print(f"Total Wins: {total_wins}")
    print(f"Total Guesses Made: {total_guesses}")
    
    if total_wins > 0:
        avg_guesses = total_guesses / total_wins
        print(f"Average Guesses Per Win: {avg_guesses:.2f}")
    
    if highest_rank:
        print(f"Highest Rank Achieved: {highest_rank}")
    
    print("=" * 60 + "\n")


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


def play_single_game(player_name, game_number, current_streak):
    """
    Play a single round of the guessing game.
    
    Returns:
        tuple: (won: bool, guess_count: int)
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
            return False, guess_count - 1, True  # (won, guesses, quit)
        
        # Check if correct
        if guess == target_number:
            print_feedback(player_name, guess, target_number, is_correct=True)
            logger.info(f"Player won in {guess_count} guesses")
            return True, guess_count, False  # (won, guesses, quit)
        
        # Give feedback
        print_feedback(player_name, guess, target_number, is_correct=False)
    
    # Out of guesses
    logger.info("Player lost - out of guesses")
    return False, MAX_GUESS_COUNT, False  # (won, guesses, quit)


# ============================================================================
# MAIN GAME LOOP
# ============================================================================

def main():
    """Main game loop managing streaks and statistics."""
    logger.info("Application started")
    
    print_header()
    player_name = get_player_name()
    
    # Game statistics
    current_streak = 0
    best_streak = 0
    total_games = 0
    total_wins = 0
    total_guesses = 0
    highest_rank = None
    
    # Main game loop
    while True:
        total_games += 1
        
        # Play a single game
        won, guess_count, player_quit = play_single_game(player_name, total_games, current_streak)
        
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
            
            # Check for rank milestone
            reached_milestone, rank_name = check_rank_milestone(old_streak, current_streak)
            if reached_milestone:
                display_streak_milestone(current_streak, rank_name)
                highest_rank = rank_name
        
        # Handle loss
        else:
            # Get the target number from the previous game for display
            # target = random.randint(MIN_NUMBER, MAX_NUMBER)  # We don't actually store it, this is a placeholder
            # Any way to get most recent local variable printed here?
            display_loss("?", current_streak)
            
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
    logger.info(f"Application finished. Games: {total_games}, Wins: {total_wins}, Best Streak: {best_streak}")


if __name__ == "__main__":
    main()
