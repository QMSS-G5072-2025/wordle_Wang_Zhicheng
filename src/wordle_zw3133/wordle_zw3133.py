def validate_guess(guess, word_length=5):
    """
    Validates if a guess is valid for Wordle.

    Parameters
    ----------
    guess : str
        The word guess to validate.
    word_length : int, optional
        Expected length of the word (default 5).

    Returns
    -------
    bool
        True if guess is valid, False otherwise.

    Examples
    --------
    >>> validate_guess("apple")
    True
    >>> validate_guess("APPLE")
    False
    >>> validate_guess("app")
    False
    """
    if not isinstance(guess, str):
        return False
    if len(guess) != word_length:
        return False
    if not guess.isalpha():
        return False
    return guess.islower()


def check_guess(secret_word, guess):
    """
    Checks a guess against the secret word and returns color hints.

    Parameters
    ----------
    secret_word : str
        The secret word to guess.
    guess : str
        The player's guess.

    Returns
    -------
    list
        List of tuples (letter, color) where color is 'green', 'yellow', or 'gray'.
    """
    Examples
    --------
    >>> check_guess("apple", "apply")
    [('a', 'green'), ('p', 'green'), ('p', 'green'), ('l', 'yellow'), ('y', 'gray')]
    """
    if len(secret_word) != len(guess):
        return []

    result = []
    secret_list = list(secret_word)
    guess_list = list(guess)

    # First pass: mark exact matches (green)
    for i in range(len(guess_list)):
        if guess_list[i] == secret_list[i]:
            result.append((guess_list[i], 'green'))
            secret_list[i] = None
            guess_list[i] = None
        else:
            result.append((guess_list[i], None))

    # Second pass: mark partial matches (yellow)
    for i in range(len(guess_list)):
        if guess_list[i] is not None:
            if guess_list[i] in secret_list:
                result[i] = (guess_list[i], 'yellow')
                secret_list[secret_list.index(guess_list[i])] = None
            else:
                result[i] = (guess_list[i], 'gray')

    return result


def is_valid_word(word, word_list):
    """Checks if a word exists in the valid word list."""
    return word.lower() in [w.lower() for w in word_list]


def calculate_game_score(guesses_used, max_guesses=6):
    """Calculates the score for a completed Wordle game."""
    if guesses_used <= 0 or guesses_used > max_guesses:
        return 0
    return max_guesses - guesses_used + 1
