from wordle_zw3133 import wordle_zw3133

import pytest
from wordle_Wang_Zhicheng.wordle import (
    validate_guess,
    check_guess,
    is_valid_word,
)

# Word list for testing
WORD_LIST = [
    "crane", "apple", "hello", "world", "python",
    "house", "water", "light", "music", "dream",
    "happy", "smile", "peace", "heart", "brain",
    "table", "chair", "phone", "paper", "green"
]


# =============================================================================
# PART 1: BASIC TESTING
# =============================================================================

def test_validate_guess():
    """Test validity rules for guessing."""
    assert validate_guess("crane", 5) is True          # valid
    assert validate_guess("car", 5) is False           # too short
    assert validate_guess("craness", 5) is False       # too long
    assert validate_guess("cr@ne", 5) is False         # invalid char
    assert validate_guess("CRANE", 5) is False         # uppercase rejected
    assert validate_guess("", 5) is False
    assert validate_guess(None, 5) is False


def test_check_guess_basic():
    """Test color feedback rules."""
    assert check_guess("crane", "crane") == [
        ('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')
    ]

    assert check_guess("crane", "blimp") == [
        ('b', 'gray'), ('l', 'gray'), ('i', 'gray'), ('m', 'gray'), ('p', 'gray')
    ]

    assert check_guess("crane", "react") == [
        ('r', 'yellow'), ('e', 'yellow'), ('a', 'green'), ('c', 'yellow'), ('t', 'gray')
    ]

    # Length mismatch → returns empty list
    assert check_guess("crane", "toy") == []


def test_is_valid_word():
    """Case-insensitive dictionary membership."""
    assert is_valid_word("crane", WORD_LIST) is True
    assert is_valid_word("CrAnE", WORD_LIST) is True
    assert is_valid_word("xxxxx", WORD_LIST) is False
    assert is_valid_word("", WORD_LIST) is False


# =============================================================================
# PART 2: ADVANCED TESTING
# =============================================================================

@pytest.mark.parametrize("secret_word,guess,expected", [
    ("crane", "crane", [('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]),
    ("crane", "blimp", [('b', 'gray'), ('l', 'gray'), ('i', 'gray'), ('m', 'gray'), ('p', 'gray')]),
    ("crane", "react", [('r', 'yellow'), ('e', 'yellow'), ('a', 'green'), ('c', 'yellow'), ('t', 'gray')]),
    ("apple", "paper", [('p', 'yellow'), ('a', 'yellow'), ('p', 'green'), ('e', 'yellow'), ('r', 'gray')]),
])
def test_check_guess_comprehensive(secret_word, guess, expected):
    """Comprehensive mixed feedback cases."""
    result = check_guess(secret_word, guess)
    assert result == expected


@pytest.fixture
def common_word_list():
    """Reusable word list fixture."""
    return list(WORD_LIST)


def test_word_list_fixture(common_word_list):
    """Test fixture usage with is_valid_word."""
    for w in ["apple", "world", "music"]:
        assert is_valid_word(w, common_word_list) is True
    for w in ["zzzzz", "abcde"]:
        assert is_valid_word(w, common_word_list) is False
