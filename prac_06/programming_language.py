"""
Estimated: 30 minutes
Actual: 20mins
"""

class ProgrammingLanguage:
    """Represent programming language with key features."""
    def __init__(self, language, typing, reflection, year=0):
        """Initialize language instance."""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the language is dynamic."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the language."""
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"