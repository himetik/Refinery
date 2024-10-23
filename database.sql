"""Silo database tables"""

DROP TABLE IF EXISTS sentences;


CREATE TABLE sentences (
    id SERIAL PRIMARY KEY,
    sentence TEXT NOT NULL UNIQUE,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);
