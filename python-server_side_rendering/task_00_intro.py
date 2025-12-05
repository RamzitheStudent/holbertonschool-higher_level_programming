import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries, got {type(attendees).__name__}.")
        return

    # Handle empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        invitation = template  # Start with a copy of the template

        # Replace placeholders with attendee data, using "N/A" if missing or None
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))

        # Define output filename
        output_filename = f"output_{index}.txt"

        try:
            # Write invitation to file
            with open(output_filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
