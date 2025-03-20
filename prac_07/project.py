class Project:
    """Represent a project."""
    def __init__(self, name, start_date, priority, estimated_cost,completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimated_cost = estimated_cost
        self.completion_percentage = completion_percentage
