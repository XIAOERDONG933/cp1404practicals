class Project:
    """Represent a project."""
    def __init__(self, name, start_date, priority, estimated_cost,completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimated_cost = estimated_cost
        self.completion_percentage = completion_percentage

    def is_complete(self):
        """Determine if the project is complete."""
        return self.completion_percentage == 100

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, estimated cost: {self.estimated_cost}, "
                f"estimate: ${self.estimated_cost:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def set_percentage(self,new_percentage):
        """set percentage with new percentage."""
        self.completion_percentage = new_percentage

    def set_priority(self,new_priority):
        self.priority = new_priority