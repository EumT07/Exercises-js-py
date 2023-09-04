class Celular():
    def __init__(self,model,brand,color,price):
        self.model = model
        self.brand = brand
        self.color = color
        self.price = price

    #method
    def call(self):
        num = int(input("Insert number: "))
        print(F"Calling this number: {num}")
        
    def close(self):
        print("Hangin up the call")

    def __str__(self):
        return f"""\nCelular: {self.brand}\nModel: {self.model}\nColor: {self.color}\nPrice: {self.price}"""

nokia = Celular("546 pro","Nokia", "white",160)
samsung = Celular("A30s","Samsung","Red",180)

print(nokia)
print(samsung)

nokia.call()
