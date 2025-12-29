"""
Mood Tracker Data Models

This module defines the data models for the mood tracker application.
"""
from datetime import datetime
from typing import Optional


class MoodEntry:
    """
    Represents a single mood log entry with date, mood, and optional note.

    Attributes:
        id (str): Unique identifier for the mood entry
        date (datetime): The date and time when the mood was recorded
        mood (str): The selected mood from predefined options
        note (str): Optional text note about the mood entry
    """

    def __init__(self, mood: str, note: Optional[str] = None, entry_id: Optional[str] = None):
        """
        Initialize a MoodEntry instance.

        Args:
            mood (str): The mood to record (required)
            note (str, optional): An optional note about the mood
            entry_id (str, optional): Unique identifier (generated if not provided)
        """
        self.validate_mood(mood)

        self.id = entry_id or self._generate_id()
        self.date = datetime.now()
        self.mood = mood
        self.note = self._validate_note(note)

    def _generate_id(self) -> str:
        """
        Generate a unique identifier for the mood entry.

        Returns:
            str: A unique identifier string
        """
        import uuid
        return str(uuid.uuid4())

    def _validate_note(self, note: Optional[str]) -> Optional[str]:
        """
        Validate the note field according to business rules.

        Args:
            note (str, optional): The note to validate

        Returns:
            str: The validated note or None if empty

        Raises:
            ValueError: If the note exceeds the maximum length
        """
        if note is None:
            return None

        if len(note) > 500:
            raise ValueError("Note must be 500 characters or less")

        return note

    @staticmethod
    def validate_mood(mood: str) -> None:
        """
        Validate that the mood is one of the predefined options.

        Args:
            mood (str): The mood to validate

        Raises:
            ValueError: If the mood is not in the predefined list
        """
        predefined_moods = ["Happy", "Sad", "Neutral", "Stressed", "Excited", "Anxious", "Calm", "Angry"]

        if not mood:
            raise ValueError("Mood is required and cannot be empty")

        if mood not in predefined_moods:
            raise ValueError(f"Mood must be one of: {', '.join(predefined_moods)}")

    def to_dict(self) -> dict:
        """
        Convert the MoodEntry to a dictionary representation.

        Returns:
            dict: Dictionary representation of the MoodEntry
        """
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'mood': self.mood,
            'note': self.note
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a MoodEntry from a dictionary representation.

        Args:
            data (dict): Dictionary containing mood entry data

        Returns:
            MoodEntry: A new MoodEntry instance
        """
        # Parse the date from ISO format
        date_str = data.get('date')
        if date_str:
            date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        else:
            date_obj = datetime.now()

        # Create the MoodEntry
        entry = cls(
            mood=data['mood'],
            note=data.get('note'),
            entry_id=data.get('id')
        )
        entry.date = date_obj
        return entry