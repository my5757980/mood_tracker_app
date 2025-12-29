# API Contracts: Mood Tracker App

## Mood Entry Management

### Add Mood Entry
- **Operation**: Create a new mood entry
- **Input**: mood (string, required), note (string, optional)
- **Output**: success status, entry ID
- **Error cases**: Invalid mood value, note too long

### Get All Mood Entries
- **Operation**: Retrieve all mood entries
- **Input**: none
- **Output**: list of mood entries, sorted by date (newest first)
- **Error cases**: none (returns empty list if no entries)

### Delete Mood Entry
- **Operation**: Remove a mood entry by ID
- **Input**: entry ID (string, required)
- **Output**: success status
- **Error cases**: Entry ID not found