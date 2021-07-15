import math 
class Polygon():
    def __init__(self, n,r):
        self.n = n
        self.r = r

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

p = Polygon(2,3)
print(p.area())