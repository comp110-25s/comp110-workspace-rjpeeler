"""Program for wordle."""

__author__: str = "730654352"


def contains_char(strsearch: str, char: str) -> bool:
    """Searches for a specific character within a string."""
    assert len(char) == 1, f"len('{char}') is not 1"

    index = 0

    while index < len(strsearch):
        if strsearch[index] == char:
            return True
        else:
            index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Codifies the results of a guess, just like Wordle."""
    assert len(guess) == len(guess), "Guess must be same length as secret"
    guess_list = list(guess)
    index = 0
    while index < len(guess):
        if contains_char(secret, guess[index]) is True:
            guess_list[index] = "\U0001F7E8"
        else:
            guess_list[index] = "\U00002B1C"
        index += 1
    index = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            guess_list[index] = "\U0001F7E9"
        index += 1

    return "".join(guess_list)


def input_guess(expected_length: int) -> str:
    guess = input(f"Enter a {expected_length} character word:")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    N = 1
    while N < 7:
        print(f"===Turn {N}/6===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {N}/6 turns!")
            N = 8
        else:
            N += 1
    if N == 7:
        print("X/6 - Sorry, try again tomorrow!")
