"""Text validation."""

from typing import Tuple, Dict
import re
from app.src.refiner.refiner_config import MIN_TEXT_LENGTH, MAX_TEXT_LENGTH


def validate_text_length(text: str) -> Tuple[bool, str]:
    text_length = len(text)

    if text_length < MIN_TEXT_LENGTH:
        return False, f"Text length is too short. Minimum length is {MIN_TEXT_LENGTH}"

    if text_length > MAX_TEXT_LENGTH:
        return False, f"Text length is too long. Maximum length is {MAX_TEXT_LENGTH}"

    return True, ""


def validate_english_letters(text: str) -> Tuple[bool, str]:
    if not re.match(r'^[a-zA-Z\s]*$', text):
        return False, "Text contains non-English letters or special characters"
    return True, ""


def validate_text(text: str) -> Dict:
    if not isinstance(text, str):
        return {
            'is_valid': False,
            'errors': ['Input must be a string']
        }

    errors = []

    length_valid, length_error = validate_text_length(text)
    if not length_valid:
        errors.append(length_error)

    eng_valid, eng_error = validate_english_letters(text)
    if not eng_valid:
        errors.append(eng_error)

    return {
        'is_valid': len(errors) == 0,
        'errors': errors
    }
