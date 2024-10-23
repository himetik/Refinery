"""Text separation. Input: Text → Output: List of Sentences."""

import spacy
from typing import List
from app.src.refiner.refiner_config import LANGUAGE_MODEL


nlp = spacy.load(LANGUAGE_MODEL)


def clean_text(text: str) -> str:

    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    text = text.replace('\n', ' ')

    return ' '.join(text.split()).strip()


def split_into_sentences(text: str) -> List[str]:

    if not text:
        return []

    cleaned_text = clean_text(text)
    if not cleaned_text:
        return []

    doc = nlp(cleaned_text)
    return [sent.text.strip() for sent in doc.sents if sent.text.strip()]
