"""Text separation. Input: Text → Output: List of Sentences."""

import spacy
from typing import List, Optional
from app.src.refiner.refiner_config import LANGUAGE_MODEL


class TextSeparator:
    def __init__(self, language_model: str = LANGUAGE_MODEL):
        self.nlp = spacy.load(language_model)

    def clean_text(self, text: str) -> str:
        if not isinstance(text, str):
            raise ValueError("Input must be a string")

        text = ' '.join(text.split())
        return text.strip()

    def split_into_sentences(self, text: Optional[str]) -> List[str]:
        if not text:
            return []

        try:
            cleaned_text = self.clean_text(text)
            if not cleaned_text:
                return []

            doc = self.nlp(cleaned_text)
            return [sent.text.strip() for sent in doc.sents 
                   if sent.text.strip() and len(sent.text.split()) > 1]

        except Exception as e:
            print(f"Error processing text: {str(e)}")
            return []

