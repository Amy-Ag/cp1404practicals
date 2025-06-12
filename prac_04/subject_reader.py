"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            subjects.append(parts)
    return subjects


def display_subject_details(subjects):
    """Display each subject's details in sentence."""
    for subject_code, lecturer, students in subjects:
        print(f"{subject_code} is taught by {lecturer} and has {students} students")

main()