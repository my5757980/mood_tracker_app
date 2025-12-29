"""
Mood Tracker Service

This module provides the core business logic and data management for the mood tracker application.
It handles storing and managing MoodEntry instances using in-memory storage.
"""
from typing import List, Optional
from data.models import MoodEntry


class MoodTracker:
    """
    The main application component that manages mood entries and provides methods
    for adding, retrieving, and deleting mood entries using in-memory storage.
    """

    def __init__(self):
        """
        Initialize the MoodTracker with an empty list of mood entries.
        """
        self._entries: List[MoodEntry] = []

    def add_mood_entry(self, mood: str, note: Optional[str] = None) -> MoodEntry:
        """
        Creates and stores a new MoodEntry.

        Args:
            mood (str): The mood to record (required)
            note (str, optional): An optional note about the mood

        Returns:
            MoodEntry: The newly created MoodEntry instance

        Raises:
            ValueError: If the mood is invalid or note exceeds length limit
        """
        try:
            # Create a new MoodEntry instance
            entry = MoodEntry(mood=mood, note=note)
            # Add to the in-memory storage
            self._entries.append(entry)
            return entry
        except ValueError as e:
            # Re-raise the exception to be handled by the caller
            raise e

    def get_all_mood_entries(self) -> List[MoodEntry]:
        """
        Returns all stored entries in chronological order (newest first).

        Returns:
            List[MoodEntry]: List of all mood entries sorted by date (newest first)
        """
        # Sort entries by date in descending order (newest first)
        return sorted(self._entries, key=lambda entry: entry.date, reverse=True)

    def delete_mood_entry(self, entry_id: str) -> bool:
        """
        Removes a specific mood entry by ID.

        Args:
            entry_id (str): The ID of the entry to delete

        Returns:
            bool: True if the entry was found and deleted, False otherwise
        """
        for i, entry in enumerate(self._entries):
            if entry.id == entry_id:
                del self._entries[i]
                return True
        return False

    def get_mood_entry_by_id(self, entry_id: str) -> Optional[MoodEntry]:
        """
        Retrieves a specific mood entry by ID.

        Args:
            entry_id (str): The ID of the entry to retrieve

        Returns:
            MoodEntry: The mood entry if found, None otherwise
        """
        for entry in self._entries:
            if entry.id == entry_id:
                return entry
        return None

    def get_mood_count(self) -> int:
        """
        Get the total number of mood entries.

        Returns:
            int: The number of mood entries
        """
        return len(self._entries)

    def get_moods_by_type(self, mood_type: str) -> List[MoodEntry]:
        """
        Get all entries of a specific mood type.

        Args:
            mood_type (str): The mood type to filter by

        Returns:
            List[MoodEntry]: List of mood entries matching the specified type
        """
        return [entry for entry in self._entries if entry.mood == mood_type]