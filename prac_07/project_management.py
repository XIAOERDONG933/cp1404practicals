"""
Estimated time: 40 min
Actual time: 60 min
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
            handle_update_projects(projects)
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


def handle_update_projects(projects):
    """Handle updating projects"""
    for idx,project in enumerate(projects):
        print(f"{idx} {project}")
    choice = int(input("Project choice: "))
    # TODO Error check the input choice
    current_project = projects[choice]
    print(current_project)
    set_project_info(current_project, 'percentage')
    set_project_info(current_project, 'priority')


def set_project_info(project, info):
    """Set new project new percentage or priority"""
    new_info = input(f"New Project {info.title()}: ")
    if info != '':
       if info == 'percentage':
           project.set_percentage(int(new_info))
       elif info == 'priority':
           project.set_priority(int(new_info))



main()