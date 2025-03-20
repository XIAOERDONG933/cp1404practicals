"""
Estimated time: 40 min
Actual time: 60 min
"""
import datetime
from project import Project

FILENAME = 'projects.txt'
HEADER = ['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage']

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    display_menu()
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l': #load
            projects = handle_load_projects()
        elif choice == 's': #save
            handle_save_projects(projects)
        elif choice == 'd': #display
            handle_display_projects(projects)
        elif choice == 'f': #filter by date
            handle_filter_project(projects)
        elif choice == 'a': #add
            handle_add_project(projects)
        elif choice == 'u': #update
            handle_update_projects(projects)
        else:
            print("Invalid choice")
        display_menu()
        choice = input(">>> ").lower()
    handle_quit()


def convert_start_date(start_date):
    """Convert start date into datetime"""
    return datetime.datetime.strptime(start_date, "%d/%m/%Y").date()


def load_projects(filename=FILENAME):
    """Load projects from file"""
    projects = []
    in_file = open(filename,"r")
    in_file.readline()
    for line in in_file:
       parts = line.strip().split('\t')
       formatted_start = convert_start_date(parts[1])
       # name, start date, priority, cost, completion percentage
       project = Project(parts[0], formatted_start, int(parts[2]), float(parts[3]), int(parts[4]))
       projects.append(project)
    in_file.close()
    return projects


def handle_load_projects():
    """Handle loading projects from file"""
    filename = input("Filename:")
    return load_projects(filename)


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


def handle_add_project(projects):
    """Handle adding new project"""
    print("Let's add a new project")
    name = input("Name: ")
    start = input("Start date (dd/mm/yy): ")
    converted_start = convert_start_date(start)
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate： $ "))
    percentage = int(input("Percentage complete: "))
    new_project = Project(name, converted_start, priority, cost, percentage)
    projects.append(new_project)


def handle_filter_project(projects):
    """Handle filtering projects by date"""
    input_date = input("Show projects that start after date (dd/mm/yy): ")
    converted_input_date = convert_start_date(input_date)
    result_projects = []
    for project in projects:
        if project.start_date > converted_input_date:
            result_projects.append(project)
    for project in result_projects:
        print(project)

def save_projects(projects, filename=FILENAME):
    """Save projects to file"""
    with open(filename,"w") as out_file:
        out_file.write("\t".join(HEADER) + "\n")
        for project in projects:
            converted_start = project.start_date.strftime("%d/%m/%Y")
            out_file.write(f"{project.name}\t{converted_start}\t"
                           f"{project.priority}\t{project.cost}\t"
                           f"{project.percentage}\n")


def handle_save_projects(projects):
    """Handle saving projects"""
    filename = input("Filename: ")
    save_projects(projects, filename)


def handle_quit():
    """Handle quit"""
    ans = input(f"Would you like to save to {FILENAME}? ").lower()
    if ans == 'y' or ans == 'yes':
        save_projects(projects)
    print("Thank you for using custom-built project management software.")

main()