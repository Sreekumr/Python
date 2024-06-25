
class Human:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def Printname(self):
        print(" Hellooo " + self.fname + " " + self.lname)

class Student(Human):
    
    def __init__(self, fname, lname):
        #Human.__init__(fname, lname)
        super().__init__(fname, lname)
    
obj = Student("hari","K A")
obj.Printname()  