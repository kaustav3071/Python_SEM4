# Initialize the event management system
event_management = {}

# Function to add an event with participants
def add_event(event_name, participants_list):
    event_management[event_name] = participants_list
    print(f"Event '{event_name}' added successfully!")

# Function to display participants of a specific event
def display_participants(event_name):
    if event_name in event_management:
        print(f"Participants for Event '{event_name}':")
        for participant in event_management[event_name]:
            print(f"Name: {participant[0]}, Contact: {participant[1]}, Department: {participant[2]}, Status: {participant[3]}")
    else:
        print(f"Event '{event_name}' not found!")

# Function to search for a participant by name
def search_participant(participant_name):
    found = False
    for event_name, participants in event_management.items():
        for participant in participants:
            if participant[0] == participant_name:
                print(f"Participant Found in Event '{event_name}':")
                print(f"Name: {participant[0]}, Contact: {participant[1]}, Department: {participant[2]}, Status: {participant[3]}")
                found = True
    if not found:
        print(f"Participant '{participant_name}' not found in any event.")

# Function to mark a participant's attendance
def mark_attendance(event_name, participant_name, status):
    if event_name in event_management:
        for participant in event_management[event_name]:
            if participant[0] == participant_name:
                participant_list = list(participant)
                participant_list[3] = status
                event_management[event_name][event_management[event_name].index(participant)] = tuple(participant_list)
                print(f"Attendance for '{participant_name}' updated to '{status}' in Event '{event_name}'.")
                return
        print(f"Participant '{participant_name}' not found in Event '{event_name}'.")
    else:
        print(f"Event '{event_name}' not found!")

# Function to generate a summary of total participants in each event
def generate_summary():
    print("Event Participation Summary:")
    for event_name, participants in event_management.items():
        print(f"Event: {event_name}, Total Participants: {len(participants)}")

# Main program
if __name__ == "__main__":
    # Adding sample events and participants
    add_event("Coding Competition", [
        ("Alice", "1234567890", "CS", "Not Attended"),
        ("Bob", "9876543210", "IT", "Not Attended"),
        ("Charlie", "5555555555", "ECE", "Not Attended")
    ])
    add_event("Debate", [
        ("Alice", "1234567890", "CS", "Not Attended"),
        ("David", "9999999999", "ME", "Not Attended")
    ])

    # Display participants of a specific event
    display_participants("Coding Competition")

    # Search for a participant by name
    search_participant("Alice")

    # Mark a participant's attendance
    mark_attendance("Coding Competition", "Alice", "Attended")

    # Generate a summary of total participants in each event
    generate_summary()