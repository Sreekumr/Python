class Animal:
    def eat(self):
        print("This animal...")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating...")


rabbit = Rabbit()
rabbit.eat()