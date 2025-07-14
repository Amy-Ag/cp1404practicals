"""
Estimate: 10 mins
Actual: 7mins
"""

from datetime import datetime
COMPLETE_PERCENTAGE=100

class Project:
    """Represent project with attributes."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize project with attributes."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def is_complete(self):
        """Return True if project is complete."""
        return self.completion_percentage == COMPLETE_PERCENTAGE

    def __lt__(self, other):
        """Sort projects by priority."""
        return self.priority < other.priority

    def __str__(self):
        """Return string representation of project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}"
                f", priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")