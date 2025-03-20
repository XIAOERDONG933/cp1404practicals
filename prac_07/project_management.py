"""
Estimated time:
Actual time:
"""
from project import Project

FILENAME = 'projects.txt'

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    display_menu()
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l': #load
            pass
        elif choice == 's': #save
            pass
        elif choice == 'd': #display
            handle_display_projects(projects)
        elif choice == 'f': #filter by date
            pass
        elif choice == 'a': #add
            pass
        elif choice == 'u': #update
            pass
        else:
            print("Invalid choice")
        display_menu()
        choice = input(">>> ").lower()



def load_projects(filename=FILENAME):
    """Load projects from file"""
    projects = []
    in_file = open(filename,"r")
    in_file.readline()
    for line in in_file:
       parts = line.strip().split('\t')
       # name, start date, priority, cost, completion percentage
       project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
       projects.append(project)
    in_file.close()
    return projects


def display_menu():
    """Display menu"""
    print("""- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit""")

def handle_display_projects(projects):
    """Handle displaying projects"""
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if project.is_complete():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    complete_projects.sort()
    incomplete_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Complete projects:")
    for project in complete_projects:
        print(f"  {project}")


main()