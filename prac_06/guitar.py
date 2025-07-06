"""
Estimated: 40 minutes
Actual: 30mins
"""

class Guitar:
    """Represent guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """Initialize guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Convert into string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, year):
        """Return age in years."""
        return  year - self.year

    def is_vintage(self, year):
        """Return True if guitar is more than 50 y/o."""
        return self.get_age(year)>=50
