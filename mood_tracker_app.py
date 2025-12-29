"""
Mood Tracker Application

A Streamlit web application that allows users to track their moods over time.
Users can log moods with optional notes, view mood history, and delete entries.
"""
import streamlit as st
from datetime import datetime
from data.mood_tracker import MoodTracker
from data.models import MoodEntry


# Initialize the mood tracker in session state if not already present
if 'mood_tracker' not in st.session_state:
    st.session_state.mood_tracker = MoodTracker()

# Set up the Streamlit page configuration
st.set_page_config(page_title="Mood Tracker", page_icon="😊", layout="wide")
st.title("😊 Mood Tracker App")
st.markdown("---")

# Create tabs for different functionalities
tab1, tab2 = st.tabs(["Log Mood", "View History"])

# Tab 1: Log Mood (User Story 1 - US1)
with tab1:
    st.header("Log Your Mood")

    # Create mood selection dropdown (T011)
    mood_options = ["Happy", "Sad", "Neutral", "Stressed", "Excited", "Anxious", "Calm", "Angry"]
    selected_mood = st.selectbox("How are you feeling today?", mood_options, key="mood_select")

    # Create optional note text area (T012)
    note = st.text_area("Add a note about your day (optional)", max_chars=500, key="note_input")

    # Create save mood button with event handling (T013)
    if st.button("Save Mood", key="save_mood_btn"):
        try:
            # Connect mood input UI to MoodTracker service add_mood_entry method (T014)
            # Add input validation for mood selection and note length in UI (T015, T016)
            mood_entry = st.session_state.mood_tracker.add_mood_entry(selected_mood, note if note.strip() else None)
            st.success(f"✅ Mood '{mood_entry.mood}' saved successfully!")
        except ValueError as e:
            st.error(f"❌ Error: {str(e)}")
        except Exception as e:
            st.error(f"❌ An unexpected error occurred: {str(e)}")

# Tab 2: View Mood History (User Story 2 - US2)
with tab2:
    st.header("Mood History")

    # Get all mood entries (T018)
    all_entries = st.session_state.mood_tracker.get_all_mood_entries()

    # Add empty state message when no mood entries exist (T021)
    if not all_entries:
        st.info("📝 No mood entries yet. Start by logging your first mood!")
    else:
        # Display mood entries in chronological order (newest first) (T020)
        st.subheader(f"Showing {len(all_entries)} mood entries")

        # Format mood entries for display with date, mood, and note (T019)
        for entry in all_entries:
            # Create a container for each mood entry
            with st.container():
                # Format the date for display
                formatted_date = entry.date.strftime("%Y-%m-%d %H:%M")

                # Create columns for layout
                col1, col2, col3, col4 = st.columns([2, 2, 3, 1])

                # Display mood and date
                col1.write(f"**{entry.mood}**")
                col2.write(f"_{formatted_date}_")

                # Display note if it exists
                if entry.note:
                    col3.write(f"_{entry.note}_")
                else:
                    col3.write("_No note_")

                # Add delete button to each mood entry (T023)
                if col4.button("🗑️ Delete", key=f"delete_{entry.id}"):
                    # Implement delete confirmation dialog (T024)
                    if st.session_state.get(f"confirm_delete_{entry.id}", False):
                        # Connect delete functionality to MoodTracker service delete_mood_entry method (T025)
                        success = st.session_state.mood_tracker.delete_mood_entry(entry.id)
                        if success:
                            st.success("Entry deleted successfully!")
                            # Use Streamlit's experimental rerun to refresh the display
                            st.rerun()
                        else:
                            st.error("Failed to delete entry.")
                    else:
                        # Set confirmation flag
                        st.session_state[f"confirm_delete_{entry.id}"] = True
                        st.warning(f"Click again to confirm deletion of '{entry.mood}' entry")

                # If user clicked delete but hasn't confirmed yet, show a way to cancel
                if st.session_state.get(f"confirm_delete_{entry.id}", False):
                    if st.button("Cancel Deletion", key=f"cancel_delete_{entry.id}"):
                        st.session_state[f"confirm_delete_{entry.id}"] = False
                        st.rerun()

                st.divider()

# Improve UI layout and styling for better user experience (T029)
st.markdown("---")
st.markdown("### 💡 Tips")
st.markdown("- Log your mood regularly to track patterns over time")
st.markdown("- Add notes to remember what influenced your mood")
st.markdown("- Delete entries you no longer need")

# Add comprehensive error handling throughout the application (T030)
st.markdown("---")
st.markdown("### 📊 Stats")
total_entries = st.session_state.mood_tracker.get_mood_count()
st.write(f"Total mood entries logged: **{total_entries}**")

# Footer
st.markdown("---")
st.markdown("😊 Mood Tracker App - Track your emotional journey")