from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Silver service taxi that includes flagfall cost and fanciness."""
    flagfall = 4.50
    def __init__(self,name,fuel,fanciness):
        """Initialise SilverServiceTaxi."""
        super().__init__(name,fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return total fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
