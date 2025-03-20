class Project:
    """Represent a project."""
    def __init__(self, name, start_date, priority, cost,percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def is_complete(self):
        """Determine if the project is complete."""
        return self.percentage == 100

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, estimated cost: {self.cost}, "
                f"estimate: ${self.cost:.2f}, completion: {self.percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def set_percentage(self,new_percentage):
        """set percentage with new percentage."""
        self.percentage = new_percentage

    def set_priority(self,new_priority):
        self.priority = new_priority