# Quickstart: Mood Tracker App

## Prerequisites
- Python 3.11 or higher
- pip package manager

## Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install streamlit
   ```

2. **Run the application**:
   ```bash
   streamlit run mood_tracker_app.py
   ```

3. **Access the application**:
   - Open your web browser
   - Navigate to the URL shown in the terminal (typically http://localhost:8501)

## Basic Usage

1. **Log a mood**:
   - Select a mood from the dropdown
   - Optionally add a note in the text area
   - Click "Save Mood" button

2. **View mood history**:
   - Mood entries appear in chronological order (newest first)
   - Each entry shows date, mood, and note

3. **Delete a mood entry**:
   - Click the "Delete" button next to the entry you want to remove
   - Confirm the deletion when prompted

## Manual Testing Steps (T031)

1. **Test mood logging functionality**:
   - Navigate to the "Log Mood" tab
   - Select a mood from the dropdown (e.g., "Happy")
   - Add an optional note (e.g., "Had a great day at work")
   - Click "Save Mood" button
   - Verify success message appears: "✅ Mood 'Happy' saved successfully!"

2. **Test validation**:
   - Try to save a mood with an invalid mood value (not in the dropdown options) - should not be possible due to dropdown
   - Try to add a note longer than 500 characters - should show error message

3. **Test mood history display**:
   - Navigate to the "View History" tab
   - Verify that the mood entry you saved appears in the list
   - Verify that entries are displayed in chronological order (newest first)
   - Verify that date, mood, and note are displayed correctly

4. **Test empty state**:
   - Delete all mood entries
   - Verify that the message "📝 No mood entries yet. Start by logging your first mood!" appears

5. **Test delete functionality**:
   - In the "View History" tab, click the "🗑️ Delete" button for an entry
   - Verify the confirmation message appears
   - Click again to confirm deletion
   - Verify the entry is removed from the list
   - Click "Cancel Deletion" to cancel a pending deletion

6. **Test UI elements**:
   - Verify tabs work correctly (Log Mood / View History)
   - Verify all form elements are accessible
   - Verify error messages are user-friendly

7. **Test data persistence during session**:
   - Add multiple mood entries
   - Verify they all appear in the history
   - Note: Data is stored in memory and will be lost when the app is closed

## Troubleshooting

- If the app doesn't start, ensure Streamlit is installed: `pip install streamlit`
- If you see import errors, check that all dependencies are installed
- Data is stored in memory only and will be lost when the app is closed