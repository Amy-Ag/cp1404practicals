class Band:
    """Band class."""
    def __init__(self, name):
        """Initialize band with name and empty list of members."""
        self.name = name
        self.members= []

    def add(self, musician):
        """Add musician to the band list."""
        self.members.append(musician)

    def play(self):
        """Simulate band playing."""
        for member in self.members:
            print(member.play())

    def __str__(self):
        """Return a string representation of the band instance."""
        return f"{self.name} ({','.join(str(member) for member in self.members)})"