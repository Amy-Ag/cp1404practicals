"""
Estimate: 45 minutes
Actual:
"""

from project import Project

FILENAME="projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    projects= load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}.")
    MENU= "\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(Q)uit"
    print(MENU)
    choice = input(">>>").lower()

    while choice != "q":
        if choice == "l":
            filname= input("Filename: ")
            projects= load_projects(filname)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
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
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]
    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"   {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"   {project}")

def save_projects(filename, projects):
    """Save projects to file and return as a list of Project objects."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}"
                  f"\t{project.completion_percentage}", file=out_file)

main()