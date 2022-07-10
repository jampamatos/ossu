# INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES

## TABLE OF CONTENTS

- [INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES](#introduction-to-computer-science-and-programming-using-python----notes)
  - [TABLE OF CONTENTS](#table-of-contents)
  - [UNIT 5 - OBJECT ORIENTED PROGRAMMING](#unit-5---object-oriented-programming)
    - [5.1. Classes and Inheritance](#51-classes-and-inheritance)
    - [5.2. Methods](#52-methods)
    - [5.3. Examples](#53-examples)
    - [5.4. Why OOP](#54-why-oop)
    - [5.5. Hierarchies](#55-hierarchies)

## UNIT 5 - OBJECT ORIENTED PROGRAMMING

### 5.1. Classes and Inheritance

- All data in Python (`int`, `float`, `string`, etc) are an instance of an **object**.
- All objects have:
  - A **type**
  - an internal **data representation**
  - a set of procedures for **interaction** with the object.
- each **instance** is a particular type of object:
  - `1234`is an instance of `int`
  - `a = 'hello'`, `a`is a instance of a string
- everything in Python is an **object** and has a **type**.
- objects are a **data bastraction** that capture:
  - internal **representation** through data attributes
  - **interface** for interaction with object through methods (procedures), defines behavior but hides implementation
- can **create new instances** of objects
- can **destroy** objects:
  - explicitly using `del` or just "forget" about them
  - Python system will reclaim destroyed or inaccessible objects - called "garbage collection".
- **Example:** `[1, 2, 3, 4]` is an instance of type `list`
- Lists are represented internally in the computer as a **linked lists of pair of cells**, in which the first element represent the data and the second *points* to the next index.
- This is indifferent, because we manipulate them not by their internal mechanics, but by a set of procedures.
  - internal representation should be **private*
  - correct behavior may be compromised if we manipulate internal representation -- **use defined interfaces**

- **Creating a class** involves:
  - defining the class name
  - defining class attributes
  - i.e. someone wrote code to implement a list class
- **Using** the class involves:
  - creating new instances of objects
  - doing operations on the instances
  - i.e. `l = [1, 2]` and `len(l)`
- **Advantages of OOP:**
  - bundle data into packages together with procedures that work on them through well-defined interfaces
  - *divide-and-conquer*:
    - implement and test behaviour of each class separately
    - increased modularity reduces complexity
  - class make it easy to reuse code:
    - many Python modules define new classes
    - each class has a separate environment (no collision on function names)
    - inheritance allows subclasses to redefine or extend a selected subset of a superclass' behavior

- **Class Instances:**
  - To define classes:

```python
class Coordinate(object):
  # define attributes here
```

- `object` means that `Coordinate` is a Python object and **inherits** all its attributes
  - `Coordinate` is a subclass of `object`
  - `object` is a superclass of `Coordinate`

- **Attributes:**
  - data and procedures that belong to the class
  - *data* attributes:
    - other objects that make up the class
    - e.g. a coordinate is made up of two numbers
  - procedural attributes (*methods*):
    - functions that only work with this class
    - e.g. a distance between two coordinates can be defined, but distance between two list objects have no meaning
- To create an instance of a class:

```python
class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

c = Coordinate(3,4)
origin = Coordinate(0,0)

print(c.x)
# 3

print(origin.x)
# 0
```

- `c` is poiting to a frame (like we saw with function calls)
  - within the scope of that frame we bound values to data attribute variables
  - `c.x` is interpreted as getting the value of `c` (a frame) and then looking up the value associate with `x` within that frame (thus the specific value for this instance)

### 5.2. Methods

- A **method** is a procedural attribute, like a function that *works only with this class*.
- Python will always pass the actual object as the first argument.
- Because of that, convention is to use **self** as the name of first argument of all methods.
- The `.` operator is used to access any attribute:
  - a data attribute of an object
  - a method of an object

```python
class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def distance(self, other):
    x_diff_sq = (self.x - other.x)**2
    y_diff_sq = (self.y - other.y)**2
    return (x_diff_sq + y_diff_sq)**0.5
    
c = Coordinate(3,4)
origin = Coordinate(0,0)

# Conventional way:
print(c.distance(origin))
# 5.0

# Equivalent to:
print(Coordinate.distance(c, origin))
# 5.0
```

- **Print a representation of an object:**

```python
c = Coordinate(3,4)
print(c)

# <__main__.Coordinate object at 0x7fa918510488>
```

- **uninformative** print representation by default
- define a `__str__` method for a class:
  - Python calls the `__str__` method when used `print` on that class object

```python
class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def distance(self, other):
    x_diff_sq = (self.x - other.x)**2
    y_diff_sq = (self.y - other.y)**2
    return (x_diff_sq + y_diff_sq)**0.5
  
  def __str__(self):
    return f'<{self.x},{self.y}>'
    
c = Coordinate(3,4)
print(c)
# <3,4>

print(type(c))
# <class __main__.Coordinate>

print(isinstance(c, Coordinate))
# True
```

- Custom Classes allow for customization of built-in methods:
  - `__add__(self, other)` == `self + other`
  - `__sub__(self, other)` == `self - other`
  - `__eq__(self, other)` == `self == other`
  - `__lt__(self, other)` == `self < other`
  - `__len__(self, other)` == `len(self)`
  - and [others](https://docs.python.org/2/reference/datamodel.html#basic-customization)
  
```python
class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def distance(self, other):
    x_diff_sq = (self.x - other.x)**2
    y_diff_sq = (self.y - other.y)**2
    return (x_diff_sq + y_diff_sq)**0.5
  
  def __str__(self):
    return f'<{self.x},{self.y}>'
    
  def __sub__(self, other):
    return Coordinate(self.x - other.x, self.y - other.y)
    
c = Coordinate(3,4)
d = Coordinate(1,1)

print(c - d)
# <2,3>
```

### 5.3. Examples

- **Example: Fractions**

- Create a *new type* to represent number as a fraction
- **internal representation** is two integers:
  - numerator
  - denominator
- **methods:**
  - print representation
  - add, subtract
  - convert to float

```python
class fraction(object):
  def __init__(self,numer,denom):
    self.numer = numer
    self.denom = denom
  
  def __str__(self):
    return f'{str(self.numer)}/{str(self.denom)}'
  
  def getNumer(self):
    return self.numer
  
  def getDenom(self):
    return self.denom
  
  def __add__(self,other):
    numerNew = other.getDenon() * self.getNumer() + other.getNumer() * self.getDenom()
    denomNew = other.getDenom() * self.getDenom()
    return fraction(numerNew, denomNew)
  
  def __sub__(self,other):
    numerNew = other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
    denomNew = other.getDenom() * self.getDenom()
    return fraction(numerNew, denomNew)
    
  def convert(self):
    return self.getNumer() / self.getDenom()
```

- **Example: set of integers**

- create a new type to represent a **collection of integers**
  - initially the set is empty
  - a particular integer appears only once in a set: **representational invariant** enforced by the code  
- internal **data representation**
  - use a list to store the elements of a set
- **interface:**
  - `insert(e)` - insert integer `e` into the set if not there
  - `member(e)` - returns `True` if `e` in set, `False` if not
  - `remove(e)` - remove integer `e` from set, error if not present

```python
class intSet(object):
  def __init__(self):
    self.vals = []
  
  def insert(self, e):
    if not e in self.vals:
      self.vals.append(e)
  
  def member(self, e):
    return e in self.vals
  
  def remove(self, e):
    try:
      self.vals.remove(e)
    except:
      raise ValueError(f'{e} not found')
  
  def __str__(self):
    self.val.sort()
    result = ''
    for e in self.vals:
      result += f'{e},'
    return '{' + result[:-1] + '}'
    
    # result[:-1] to remove last comma
```

### 5.4. Why OOP

- **bundle together objects** that share
  - common attributes and
  - procedures that operate on those attributes
- uses **abstraction** to make a distinct between how to implement an object vs how to use the object
- build **layers** of object abstraction that inherit behavior from other classes of objects
- create ou **own classes of objects** on top of Python's basic classes
- Groups of objects have attributes:
  - **data attributes:**
    - how can you represent your object with data?
    - **what it is**
      - for a coordinate: x and y values
      - for an animal: age and name
  - **procedual attributes:**
    - what kind of things can you write with the object?
    - **what it does**
      - for a coordinate: find distance between two
      - for an animal: make a sound

```python
class Animal(object):
  def __init__(self, age):
    self.age = age
    self.name = None
  
  def get_age(self):
    return self.age
  
  def get_name(self):
    return self.name
  
  def set_age(self, newage):
    self.age = newage
  
  def set_name(self, newname):
    self.name = newname
  
  def __str__(self):
    return f"animal:{self.name}:{self.age}"
  

my_animal = Animal(3)
print(my_animal)
# animal:None:3

my_animal.set_name('Mike')
print(my_animal)
# animal:Mike:3
```

- **dot notation** can be used to access attributes (data and methods) though it is better ti use getters and setters to access data attributes

`a.age` but `a.get_age()` **is preferred**

- **Information hiding**
  - author of class definition may change data attribute variable names

```python
class Animal(object):
  def __init__(self, age):
    self.years = age
    # replaced age data attribute by years
  
  def get_age(self):
    return self.years
```

- if you are **accessing data attriutes** outisde the class and class **definition changes**, may get errors
- outside of class, use getters and setters instead

### 5.5. Hierarchies

- **parent class** (superclass)
- **child class** (subclass)
  - inherits all data and behavior of parent class
  - add more info
  - add more behavior
  - override behavior

```python
class Animal(object):
  def __init__(self, age):
    self.age = age
    self.name = None
  
  def get_age(self):
    return self.age
  
  def get_name(self):
    return self.name
  
  def set_age(self, newage):
    self.age = newage
  
  def set_name(self, newname=''):
    self.name = newname
  
  def __str__(self):
    return f"animal:{self.name}:{self.age}"
  
class Cat(Animal):
  def speak(self):
    print('meow')
  
  def __str__(self):
    return f"cat:{self.name}:{self.age}"

class Dog(Animal):
  def speak(self):
    print('woof')
  
  def __str__(self):
    return f"dog:{self.name}:{self.age}"

jelly = Cat(1)
jelly.set_name('Jelly')
print(jelly)
# cat:Jelly:1
jelly.speak()
# meow

mike = Dog(2)
mike.set_name('Mike')
print(mike)
# dog:Mike:2
mike.speak()
# woof
```

- subclass can have **methods with same name** as superclass
- subclass can have **methods with same name** as other subclasses
- when we call a method on an object instance:
  - look for a method name in **current class definition**
  - if not found, look for method name **up the hierarchy** (in parent, then grandparent, and so on)
  - use first method up the hierarchy found under that name, throw an error if doesn't find it

```python
class Person(Animal):
  def __init__(self, name, age):
    Animal.__init__(self, age)
    Animal.set_name(self, name)
    self.friends = []
  
  def get_friends(self):
    return self.friends
  
  def add_friend(self, fname):
    if fname not in self.friends:
      self.friends.append(fname)
  
  def speak(self):
    print("Hello!")
  
  def age_diff(self, other):
    diff = self.get_age() - other.get_age()
    if self.get_age() > other.get_age():
      print(f"{self.name} is {diff} years older than {other.name}")
    else:
      print(f"{self.name} is {-diff} years younger than {other.name}")
  
  def __str__(self):
    return f"person:{self.name}:{self.age}"

class Student(Person):
  def __init__(self, name, age, major=None):
    Person.__init__(self, name, age)
    self.major = major
  
  def change_major(self, major):
    self= major
  
  def speak(self):
    r = random.random()
    if r < 0.25:
      print('I have homework')
    elif 0.25 <= r < 0.5:
      print('I need to sleep')
    elif 0.5 <= r < 0.75:
      print('I should eat')
    else:
      print("I'm playing Xbox")
  
  def __str__(self):
    return f"student:{self.name}:{self.age}:{self.major}"
    
jampa = Person("Jampa", 38)
quim = Person("Joaquim", (2022-1950))
print(jampa)
# person:Jampa:38
jampa.speak()
# Hello!
jampa.age_diff(quim)
# Jampa is 34 years younger than Joaquim

tullio = Student('Tullio', 15)
print(tullio)
# student:Tullio:15:None
tullio.age_diff(jampa)
# Tullio is 23 years younger than Jampa
tullio.speak()
# I need to sleep
```
