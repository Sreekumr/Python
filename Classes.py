

class Sem3:
    def __init__(self , Rep1,Tutor):
        self.Rep1= Rep1
        self.Tutor= Tutor
        
c1 = Sem3("Sivand","keerthy Miss")

print(c1.Rep1)
print(c1.Tutor)

class Sem2:
    ClassRep = "Revathy"
    PlacementRep = "Merin"
    def duty1(self):                     # "self" is the first parameter in every function
        print("Placement  Coordination")  # "self" is reference to the current like "this" in java   
    def MarkAttend(self):
        print("Take Attendence")
    


c2 = Sem2()

print(c2.PlacementRep)
c2.duty1()
c2.MarkAttend()

