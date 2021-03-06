class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
      newSet = intSet()

      for el in self.vals:
        if other.member(el): newSet.insert(el)
      
      return newSet
    
    def __len__(self):
      len = 0

      for el in self.vals:
        len += 1
      
      return len


newSet1 = intSet()
newSet1.insert(3)
newSet1.insert(4)
newSet1.insert(5)

newSet2 = intSet()
newSet2.insert(0)
newSet2.insert(1)
newSet2.insert(2)
newSet2.insert(3)


print(newSet1.intersect(newSet2))
print(len(newSet1))
print(len(newSet2))