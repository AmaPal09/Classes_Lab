"""Classes for melon orders."""


class AbstractMelonOrder(): 
    """An abstract base class that other Melon Orders inherit from. """
    tax = None

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
    tax = .08
    order_type = "domestic"

    # def __init__(self,species,qty): 
    #     super().__init__(species,qty)
     

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = .17
    order_type = "international"

    def __init__(self,species,qty,country_code,): 
        super().__init__(species,qty)
        self.country_code = country_code
   
    def get_total(self):
        """Calculate price, including tax."""
        if self.qty < 10:
            return super().get_total() + 3
        else:
            return super.get_total() 

    def get_country_code(self):
        """Return the country code."""
        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """Government Melon Orders that need no taxes """
    passed_inspection = False
    tax = 0 

    def mark_inspection(self,passed): 
        if passed == True:
            self.passed_inspection = True
        elif passed == False: 
            self.passed_inspection = False
        else: 
            print("Provide True or False as parameters")



    
