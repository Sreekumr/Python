

class shape:
    def __init__(self, length,breadth):
        self.length = length
        self.breadth = breadth

    def Area(self):
     return self.length * self.breadth

class shape2():
   def __init__(self, a ,b):
      self.a = a
      self.b = b
   def Area(self):
       res=self.a* self.b
       print("Area of Rectangle:",res )

class shape3():
   def __init__(self, a ,b):
      self.a = a
      self.b = b
      def Area(self):
       res= self.a* self.b       
       print("Area of Square:",res )

obj1= shape2(12,3)
obj1.Area()
   