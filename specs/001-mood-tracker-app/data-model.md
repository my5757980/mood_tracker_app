# Data Model: Mood Tracker App

## MoodEntry Entity

### Attributes
- **date**: datetime (required) - The date and time when the mood was recorded
- **mood**: string (required) - The selected mood from predefined options (Happy, Sad, Neutral, Stressed, etc.)
- **note**: string (optional) - Optional text note about the mood entry

### Validation Rules
- **date**: Must be a valid datetime object, defaults to current time if not provided
- **mood**: Must be one of the predefined mood options, required field
- **note**: Optional field, maximum 500 characters if provided

### Relationships
- None (standalone entity)

## MoodTracker Service

### Responsibilities
- Store and manage MoodEntry instances
- Provide methods for adding, retrieving, and deleting mood entries
- Handle in-memory storage using Python list/dict

### Methods
- **add_mood_entry(mood, note)**: Creates and stores a new MoodEntry
- **get_all_mood_entries()**: Returns all stored entries in chronological order (newest first)
- **delete_mood_entry(entry_id)**: Removes a specific mood entry by ID
- **get_mood_entry_by_id(entry_id)**: Retrieves a specific mood entry by ID

### State Transitions
- Mood entries are created in "active" state
- Mood entries can be transitioned to "deleted" state (removed from storage)