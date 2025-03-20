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


main()