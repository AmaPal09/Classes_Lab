"""Classes for melon orders."""


class AbstractMelonOrder(): 
    """An abstract base class that other Melon Orders inherit from. """

    def __init__(self,species,qty): 
        self.species = species
        self.qty = qty
        self.shipped = False
        

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self,species,qty,order_type = "domestic", tax = 0.08): 
        super().__init__(species,qty)
        self.order_type = order_type
        self.tax = tax

     


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self,species,qty,country_code,order_type = "international",tax = 0.17): 
        super().__init__(species,qty)
        self.country_code = country_code
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        return super().get_total() + 3


    def get_country_code(self):
        """Return the country code."""
        return self.country_code



    
