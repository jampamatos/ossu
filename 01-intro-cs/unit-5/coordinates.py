class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
      return (self.x, self.y) == (other.x, other.y)
    
    def __repr__(self):
      return f'Coordinate({self.x}, {self.y})'

coord1 = Coordinate(3,4)

print(eval(repr(coord1)) == coord1)