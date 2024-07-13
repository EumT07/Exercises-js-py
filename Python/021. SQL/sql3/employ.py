class Employee:
    """A simple employe class"""

    def __init__(self, firstName, lastName, payment):
        self.firstName = firstName
        self.lastName = lastName
        self.payment = payment


    def __str__(self):
        return f"Hi my name is: {self.firstName} {self.lastName} My payment: {self.payment}"



        