class Polygon:
    width=0
    height=0
    def set_values(self,width,height):
        Polygon.width=width
        Polygon.height=height

class Rectangle(Polygon):
    def area(self):
        print(self.width*self.height)

class Triangle(Polygon):
    def area(self):
        print((self.width*self.height)/2)
rect=Rectangle()
tri=Triangle()
rect.set_values(4,5)
tri.set_values(4,5)
rect.area()
tri.area()
    
        
