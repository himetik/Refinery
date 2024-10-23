"""Uploading to the database."""

from sqlalchemy.exc import IntegrityError
from app.src.database.base_connection import get_db_session
from app.src.database.base_models import Sentence


def insert_sentence(sentence_text: str) -> bool:

    with get_db_session() as session:
        existing_sentence = session.query(Sentence).filter_by(sentence=sentence_text).first()
        if existing_sentence:
            print(f"The sentence '{sentence_text}' already exists in the database (id: {existing_sentence.id}).")
            return False

        new_sentence = Sentence(sentence=sentence_text)
        session.add(new_sentence)
        try:
            session.commit()
            return True
        except IntegrityError as e:
            session.rollback()
            print(f"IntegrityError while adding the sentence: {e}")
            print(f"Error details: {str(e.orig)}")
            return False
        except Exception as e:
            session.rollback()
            print(f"An error occurred while adding the sentence: {e}")
            raise
