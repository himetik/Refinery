"""Text validation. Input: Text → Output: Bool (valid/invalid)."""

from typing import Dict
import re
from dataclasses import dataclass
from app.src.refiner.refiner_config import MIN_TEXT_LENGTH, MAX_TEXT_LENGTH


@dataclass
class ValidationResult:
    is_valid: bool
    errors: list[str]


def validate_text(text: str) -> Dict:
    errors = []

    if not isinstance(text, str):
        return ValidationResult(
            is_valid=False,
            errors=['Input must be a string']
        ).__dict__

    if not text or text.isspace():
        return ValidationResult(
            is_valid=False,
            errors=['Text cannot be empty or contain only whitespace']
        ).__dict__

    text_length = len(text.strip())
    if text_length < MIN_TEXT_LENGTH:
        errors.append(f"Text length is too short. Minimum length is {MIN_TEXT_LENGTH}")
    if text_length > MAX_TEXT_LENGTH:
        errors.append(f"Text length is too long. Maximum length is {MAX_TEXT_LENGTH}")

    if re.search(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]", text):
        errors.append("Text contains control characters")

    if re.search(r"\s{3,}", text):
        errors.append("Text contains too many consecutive spaces")

    return ValidationResult(
        is_valid=len(errors) == 0,
        errors=errors
    ).__dict__
