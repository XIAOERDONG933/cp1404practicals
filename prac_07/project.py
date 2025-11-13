"""
Project
Estimate: 20 minutes
Actual:   13 minutes
"""


class Project:
    """Stores information about a project"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Compare projects based on priority (lower number = higher priority)."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion_percentage == 100