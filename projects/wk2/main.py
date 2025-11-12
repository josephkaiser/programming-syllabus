"""
Repeated Number Guessing Game

This program will let the player play a game on a repeated basis to build a win streak.

The game is to guess the randomly selected integer between 1 and 10 within 3 guesses.

Every time the player succeeds in guessing the integer within 3 guesses without exceeding 3 guesses, they add to their streak.

If the streak exceeds certain levels, the player achieves a certain rank on the global scoreboard for the game.

v0.0.0.2
In progress:
    - Scoreboard feature
    - Ranks referred to in prompt
    - BIG prompts that have weight behind actions
    - Rank ups!
    - Streak callouts!

Creation Date: November 3, 2025
"""

import random
import pyfiglet
import time
import json
import os
from datetime import datetime
from log_config import setup_logger

logger = setup_logger(__name__)

MAX_GUESS_COUNT = 4  # Can tweak to make game solvable vs. luck-based
MIN_NUMBER = 1
MAX_NUMBER = 10  # 1-10 range with ~1/10 chance binary search not solvable in 4 tries
SCOREBOARD_FILE = "scoreboard.json"

RANKS = {
    0: "New kid on the block",  # Can't forget a 0 ranking for n00bz
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
    20: ":-) ",
}


# ============================================================================
# SCOREBOARD FUNCTIONS
# ============================================================================


def load_scoreboard():
    """Load the scoreboard from JSON file."""
    with open(SCOREBOARD_FILE, 'r') as f:
        data = json.load(f)
    return data


def save_scoreboard(scoreboard_data):
    """Save the scoreboard to JSON file."""
    with open(SCOREBOARD_FILE, 'w') as f:
        json.dump(scoreboard_data, f)
    return True

def add_score_entry(
    scoreboard_data, player_name, best_streak, total_games, total_wins, highest_rank
):
    """Add or update a player's score in the scoreboard."""


def get_sorted_scoreboard(scoreboard_data, sort_by="best_streak", limit=10):
    """Get sorted list of top players."""


def display_scoreboard(scoreboard_data, highlight_player=None):
    """Display the current scoreboard."""


def display_player_stats(scoreboard_data, player_name):
    """Display detailed stats for a specific player."""


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================


def print_header():
    """Display the game title and instructions."""


def print_game_start(game_number, current_streak):
    """Display the start of a new game with current streak info."""


def print_guess_prompt(guess_number):
    """Display the guess number in large text."""


def print_feedback(player_name, rank_name, guess, target, is_correct):
    """Display feedback on the player's guess."""


def display_win(guess_count, streak):
    """Show celebration for winning a game."""


def display_streak_milestone(streak, rank_name):
    """Show special celebration when reaching a rank milestone."""


def display_loss(target_number, streak):
    """Show message when player runs out of guesses."""


def display_game_over(total_games, total_wins, total_guesses, highest_rank):
    """Show final statistics and game over screen."""


def display_new_record(player_name, new_streak):
    """Display celebration for a new personal best."""


# ============================================================================
# INPUT FUNCTIONS
# ============================================================================


def get_player_name():
    """Get and validate the player's name."""
    logger.info(f"Getting player name.")
    while True:
        s = input("What is your name, player?\n > ").strip().title()
        try:
            logger.info(f"Player name: {str(s)}")
            return str(s)
        except TypeError:
            print("Please enter a valid name.")


def get_guess(guess_number):
    """Get and validate a guess from the player."""
    logger.info(f"Getting guess.")
    print(pyfiglet.figlet_format(f"Guess #{count}"))
    while True:
        s = input(prompt).strip().lower()
        if s == "q":
            return None
        try:
            logger.info(f"User input: {str(s)}")
            return float(s)
        except ValueError:
            print("Please input valid number or 'q' to quit.")


# ============================================================================
# GAME LOGIC FUNCTIONS
# ============================================================================


def get_current_rank(streak):
    """Get the current rank name based on streak."""


def check_rank_milestone(old_streak, new_streak):
    """Check if player reached a new rank milestone."""


def play_single_game(player_name, rank_name, game_number, current_streak):
    """
    Play a single round of the guessing game.

    Returns:
        tuple: (won: bool, guess_count: int, quit: bool, target_number: int)
    """


def get_player_record(scoreboard_data, player_name):
    """Get a player's best streak from the scoreboard."""


# ============================================================================
# MAIN GAME LOOP
# ============================================================================


def begin_game(count, player_name):
    logger.info(f"Beginning Game {count}: ")
    randnum = random.randint(1, 10)
    while True:
        count += 1
        game_kernel(count, randnum)


def game_kernel(count, randnum):
    if count > MAX_GUESS_COUNT:
        return None
    guess = get_guess("Guess a number between 1 and 10:", count)

    if guess == None:
        return None
    elif guess > randnum:
        # response = f"{player_name} guessed too high!"
        # response = pyfiglet.figlet_format(response)
        # print(response)
        print("-")
    elif guess < randnum:
        # response = "{player_name} guessed too low!"
        # response = pyfiglet.figlet_format(response)
        # print(response)
        print("+")
    elif guess == randnum:
        print(f"Correct! Guessed correctly in {count} guesses.")
        return count
    else:
        print(f"Error! Enter a proper number or p to pause.")
        count -= 1


def main():
    load_scoreboard()

    # import pdb; pdb.set_trace()
    # logger.info("Application started") # Initial print
    # print(pyfiglet.figlet_format("Number Guessing Game"))
    # print("This is a number guessing game. Enter a number between 1 and 10 and the program will tell you if you are too high or too low. Guess the number correctly in as few tries as you can. Win back to back games to build streaks.\n")
    # player_name = get_name("...but first. What is your name, player?\n > ")
    # streak = 0
    # count = 0
    # while streak < 3:
    #     streak = begin_game(count, player_name)
    #     # print(count)
    #     # print(player_name)
    #     # streak += 1 if count is not None else streak
    # print(pyfiglet.figlet_format("Game Over!"))
    # print(f"You won {streak} games in a row.")
    # logger.info(f"Application finished. Count: {count}.")


if __name__ == "__main__":
    main()
