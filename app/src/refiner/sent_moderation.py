"""Sentences moderation. Input: List of Sentences → Output: Bool (contains profanity/does not contain profanity)."""

import os
import spacy
from typing import Set, Tuple, List, Callable
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def moderate_text(
    text: str,
    nlp: spacy.language.Language,
    profanity_list: Set[str]
) -> Tuple[bool, List[str]]:
    if not text or not isinstance(text, str):
        return False, []

    try:
        doc = nlp(text.lower())
        profanity_found = [
            token.text for token in doc
            if token.text in profanity_list or token.lemma_ in profanity_list
        ]

        return bool(profanity_found), sorted(set(profanity_found))

    except Exception as e:
        logger.error(f"Error during text moderation: {str(e)}")
        return False, []


def load_profanities(filepath: str) -> Set[str]:
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return {line.strip().lower() for line in file if line.strip()}
    except Exception as e:
        logger.error(f"Error loading profanity list: {str(e)}")
        return set()


def load_language_model(model_name: str = "en_core_web_sm") -> spacy.language.Language:
    try:
        return spacy.load(model_name)
    except OSError:
        logger.error(f"Failed to load language model '{model_name}'")
        raise


def create_moderator() -> Callable[[str], Tuple[bool, List[str]]]:
    profanity_file = os.getenv('PROFANITY_FILE')
    if not profanity_file:
        raise ValueError("Environment variable 'PROFANITY_FILE' not set")

    nlp = load_language_model()
    profanity_list = load_profanities(profanity_file)

    def moderate(text: str) -> Tuple[bool, List[str]]:
        return moderate_text(text, nlp, profanity_list)

    return moderate
