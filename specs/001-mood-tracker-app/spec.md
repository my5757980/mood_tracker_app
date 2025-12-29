# Feature Specification: Mood Tracker App

**Feature Branch**: `001-mood-tracker-app`
**Created**: 2025-12-29
**Status**: Draft
**Input**: User description: "Build a Mood Tracker web application using Python and Streamlit. The application should allow users to: - Log their daily mood (e.g. Happy, Sad, Neutral, Stressed). - Add optional notes for each mood entry. - View a list of previously logged moods. - See mood history ordered by date. - Delete a mood entry if entered by mistake. Functional Requirements: - Users can select a mood from predefined options. - Users can optionally write a short note. - Each mood entry should store date, mood, and note. - All data should be stored in memory for Phase 1. - The UI should be simple and intuitive. Non-Functional Requirements: - The app must run locally using Streamlit. - The UI should be responsive and clean. - The app should not crash on invalid input. Phase 1 Scope: - In-memory storage only. - Single-user usage. - No login or authentication. Future phases may include persistence, analytics, and AI features."

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.

  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Log Daily Mood (Priority: P1)

As a user, I want to log my daily mood so that I can track my emotional state over time. I should be able to select from predefined mood options and optionally add a note about my day.

**Why this priority**: This is the core functionality of the app - without the ability to log moods, the app has no value.

**Independent Test**: User can successfully select a mood from predefined options, optionally add a note, and save the entry. The entry appears in the mood history with correct date and details.

**Acceptance Scenarios**:

1. **Given** user is on the mood logging page, **When** user selects a mood from predefined options and clicks save, **Then** mood entry is saved with today's date and mood
2. **Given** user is on the mood logging page, **When** user selects a mood and adds a note, **Then** mood entry is saved with both mood and note
3. **Given** user has entered invalid data, **When** user tries to save, **Then** appropriate error message is displayed without saving

---

### User Story 2 - View Mood History (Priority: P2)

As a user, I want to view my previously logged moods in chronological order so that I can see patterns in my emotional state over time.

**Why this priority**: This provides value by allowing users to see their mood history, which is essential for the tracking purpose.

**Independent Test**: User can see a list of all previously logged moods ordered by date, with mood and note information displayed clearly.

**Acceptance Scenarios**:

1. **Given** user has logged multiple moods, **When** user navigates to history view, **Then** all mood entries are displayed in chronological order (newest first)
2. **Given** user has logged moods with notes, **When** user views history, **Then** both mood and note are visible for each entry
3. **Given** user has no logged moods, **When** user views history, **Then** appropriate message is displayed indicating no entries exist

---

### User Story 3 - Delete Mood Entry (Priority: P3)

As a user, I want to delete a mood entry if I entered it by mistake or no longer want it in my history.

**Why this priority**: This allows users to maintain clean data by removing incorrect entries, though it's less critical than logging and viewing.

**Independent Test**: User can select a mood entry and delete it, with the entry being removed from the history display.

**Acceptance Scenarios**:

1. **Given** user has logged moods, **When** user selects a mood entry and confirms deletion, **Then** the entry is removed from the history
2. **Given** user wants to delete an entry, **When** user clicks delete and cancels, **Then** the entry remains unchanged
3. **Given** user has one mood entry, **When** user deletes it, **Then** the history shows appropriate message for empty state

---

### Edge Cases

- What happens when the app is closed and reopened? (Data should persist in memory during the session)
- How does system handle multiple entries for the same day? (System should allow multiple entries per day)
- What happens when user enters extremely long notes? (System should handle reasonable length limits gracefully)
- How does the app behave with invalid date inputs? (System should default to current date)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide predefined mood options for users to select from (Happy, Sad, Neutral, Stressed, etc.)
- **FR-002**: System MUST allow users to optionally add a text note to each mood entry
- **FR-003**: System MUST store mood entries with date, selected mood, and optional note
- **FR-004**: System MUST display mood history in chronological order (newest first)
- **FR-005**: System MUST provide a delete function for mood entries with confirmation
- **FR-006**: System MUST store all data in memory for Phase 1 (no persistent storage)
- **FR-007**: System MUST validate user inputs to prevent crashes from invalid data
- **FR-008**: System MUST provide a simple and intuitive UI using Streamlit

### Key Entities

- **MoodEntry**: Represents a single mood log with attributes date (timestamp), mood (string), and note (optional string)
- **MoodTracker**: The main application component that manages mood entries and provides UI for logging, viewing, and deleting entries

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully log a mood entry in under 30 seconds with a simple interface
- **SC-002**: Users can view their complete mood history with all entries properly ordered by date
- **SC-003**: 95% of user inputs are handled gracefully without application crashes
- **SC-004**: Users can successfully delete incorrect mood entries with clear confirmation
- **SC-005**: New users can understand and use all core features without additional instruction
