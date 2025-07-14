"""
Estimate: 45 minutes
Actual: 1 hour
"""
from datetime import datetime
from project import Project

FILENAME="projects.txt"
MENU= "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"

def main():
    print("Welcome to Pythonic Project Management")
    projects= load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}.")
    print(MENU)
    choice = input(">>>").lower()

    while choice != "q":
        if choice == "l":
            filename= input("Filename: ")
            projects= load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>").lower()
    save = input(f"Would you like to save to {FILENAME}? ").lower()
    if save in ("y", "yes"):
        save_projects(FILENAME, projects)

    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Load projects from file and return as a list of Project objects."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion= int(parts[4])
            project= Project(name, start_date, priority, cost_estimate, completion)
            projects.append(project)
    return projects

def display_projects(projects):
    """Display sorted incomplete and completed projects."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"   {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"   {project}")

def filter_projects(projects):
    """Filter projects based on start date and priority."""
    date_string= input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please enter as dd/mm/yyyy.")
        return
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    filtered_projects.sort()
    for project in filtered_projects:
        print(project)

def add_new_project(projects):
    """Add a new project to the list of projects."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    try:
        datetime.strptime(start_date_string, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please enter date as dd/mm/yyyy.")
        return
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    new_project = Project(name, start_date_string, priority, cost_estimate, completion)
    projects.append(new_project)

def update_project(projects):
    """Update projects based on start date and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project_to_update = projects[choice]
    except (ValueError, IndexError):
        print("Invalid project number.")
        return

    print(project_to_update)
    new_completion = input("New Percentage: ")
    if new_completion != "":
        project_to_update.completion_percentage = int(new_completion)
    new_priority = input("New Priority: ")
    if new_priority != "":
        project_to_update.priority = int(new_priority)

def save_projects(filename, projects):
    """Save projects to file and return as a list of Project objects."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}"
                  f"\t{project.completion_percentage}", file=out_file)





main()