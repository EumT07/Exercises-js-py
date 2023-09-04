class Person:
    def __init__(self,name,age,nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    def __str__(self):
        return f"{self.name} Age: {self.age} Nationality: {self.nationality}"


class Employee(Person):
    def __init__(self,name,age,nationality,job,exp):
        super().__init__(name,age,nationality)
        self.job = job
        self.exp = exp
    def __str__(self):
        return "Employee:\n" + super().__str__() + f"Job: {self.job} Exp: {self.exp} años\n"
    
# class Drive()


carlos = Employee("Carlos",23,"Venezolano","Ing Electrico",4)
andrea = Employee("Andre",25,"Colombiana","Secretaria",6)
luci = Employee("Luci",37,"Ecuatoriana","CEO",5)

employees = []
employees.extend([carlos,andrea,luci])

for user in employees:
    print(user)




