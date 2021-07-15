import math 
class Polygon(object):
    def __init__(self, n,r):
        if type(n) == int:
            if n > 2:
                self.n = n
            else:
                raise ValueError("number of side should be more than 2")
        else:
            raise TypeError("number of sides should be integer")
        if type(r) in (int,float):
            self.r = r
        else:
            raise TypeError("radius need to be number either a float or integer")

    def interiorAngle(self):
        return (self.n-2)*180/ self.n
    
    def edgeLength(self):
        return 2*self.r*math.sin(math.pi/self.n)
    
    def apothem(self):
        return self.r * math.cos(math.pi/self.n)
    
    def area(self):
        return 1/2 * self.n * self.edgeLength() * self.apothem()
    
    def perimeter(self):
        return self.n * self.edgeLength()

    def __eq__(self,other):
        if self.n == other.n and self.r == other.r:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"number of vertices {self.n} and circumradius is {self.r}"
    
    def __gt__(self,other):
        return self.n > other.n
        
p1 = Polygon(4,3)
p2 = Polygon(5,3)
print(p1.area())
print(p2)
print(p1>p2)