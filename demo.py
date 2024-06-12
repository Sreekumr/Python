class animal:
    def __init__(self,name: str):
        self.name=name
    def cry(self):
        print("Animal Crying")

class dog(animal):
    def cry(self):
        print("Dog Barking")

ob1=animal("animal")
ob2=dog("simba")

ob2.cry()
ob1.cry()