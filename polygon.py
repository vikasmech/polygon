import math 
class Polygon(object):
    """
    Base class for Polygon that includes the code to generate polygon 
    properties 
    """
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
            
    @property
    def interior_angle(self):
        return (self.n-2)*180/ self.n
    
    @property
    def side_length(self):
        return 2*self.r*math.sin(math.pi/self.n)
    
    @property
    def apothem(self):
        return self.r * math.cos(math.pi/self.n)
    
    @property
    def area(self):
        return 1/2 * self.n * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self.n * self.side_length

    @property
    def count_vertices(self):
        return self.n
    
    @property
    def count_edges(self):
        return self.n
    
    @property
    def circumradius(self):
        return self.r


    def __eq__(self,other):
        if isinstance(other, self.__class__):
            if self.n == other.n and self.r == other.r:
                return True
            else:
                return False
        else:
            return NotImplemented
    
    def __repr__(self):
        return f'Polygon(n={self.n}, R={self.r})'
    
    def __gt__(self,other):
        return self.n > other.n
        
p1 = Polygon(4,3)
p2 = Polygon(5,3)
print(p1.area)
print(p2)
print(p1>p2)