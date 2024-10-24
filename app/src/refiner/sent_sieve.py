"""Sentences filtration. Input: List of Sentences → Output: List of Valid Sentences."""

from typing import List
from app.src.refiner.sent_validation import validate_sentence
from app.src.refiner.sent_moderation import create_moderator


def filter_valid_sentences(sentences: List[str], profanity_file: str) -> List[str]:
    moderate = create_moderator(profanity_file)
    valid_sentences = []

    for sentence in sentences:
        try:
            validate_sentence(sentence)

            has_profanity, profanities = moderate(sentence)
            if has_profanity:
                print(f"Sentence skipped due to profanity: {', '.join(profanities)}")
                continue

            valid_sentences.append(sentence)

        except ValueError as e:
            print(f"Validation failed for '{sentence}': {str(e)}")
            continue

    return valid_sentences
