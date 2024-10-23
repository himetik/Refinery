"""Sentences validation."""

from typing import Callable, List


def create_validation_error(message: str) -> Exception:
    return ValueError(f"Validation error: {message}")


def validate_not_empty(sentence: str) -> None:
    if not sentence:
        raise create_validation_error("Sentence must not be empty")


def validate_length(sentence: str, min_length: int = 6, max_length: int = 180) -> None:
    if not (min_length <= len(sentence) <= max_length):
        raise create_validation_error(
            f"Sentence length must be between {min_length} and {max_length} characters"
        )


def validate_capitalization(sentence: str) -> None:
    if not sentence[0].isupper():
        raise create_validation_error("Sentence must start with a capital letter")


def validate_ending_punctuation(sentence: str) -> None:
    if not sentence[-1] in ".!?":
        raise create_validation_error("Sentence must end with '.', '!', or '?'")


def validate_word_count(sentence: str, min_words: int = 2) -> None:
    if len(sentence.split()) < min_words:
        raise create_validation_error(
            f"Sentence must consist of at least {min_words} words"
        )


def get_validation_functions() -> List[Callable[[str], None]]:
    return [
        validate_not_empty,
        validate_length,
        validate_capitalization,
        validate_ending_punctuation,
        validate_word_count
    ]


def validate_sentence(sentence: str) -> bool:
    sentence = sentence.strip()

    for validate in get_validation_functions():
        validate(sentence)

    return True
