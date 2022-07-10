# INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES

## TABLE OF CONTENTS

- [INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES](#introduction-to-computer-science-and-programming-using-python----notes)
  - [TABLE OF CONTENTS](#table-of-contents)
  - [UNIT 5 - OBJECT ORIENTED PROGRAMMING](#unit-5---object-oriented-programming)
    - [5.1. Classes and Inheritance](#51-classes-and-inheritance)
      - [5.1.1. Object Oriented Program](#511-object-oriented-program)
      - [5.1.2. Methods](#512-methods)
      - [5.1.3. Examples](#513-examples)
      - [5.1.4. Why OOP](#514-why-oop)
      - [5.1.5. Hierarchies](#515-hierarchies)
      - [5.1.6. Class Variables](#516-class-variables)
    - [5.2. An Extended Example](#52-an-extended-example)

## UNIT 5 - OBJECT ORIENTED PROGRAMMING

### 5.1. Classes and Inheritance

#### 5.1.1. Object Oriented Program

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

#### 5.1.2. Methods

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

#### 5.1.3. Examples

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

#### 5.1.4. Why OOP

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

#### 5.1.5. Hierarchies

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

#### 5.1.6. Class Variables

- **Class Variable** is declared inside a Class definition but outside all methods
- It belongs to the class and is shared among all object/instances of that class

```python
class Dog(Animal):

  tag = 1

  def __init__(self, age, parent1=None, parent2=None):
    Animal.__init__(self,age)
    self.parent1 = parent1
    self.parent2 = parent2
    self.dog_id = Dog.tag
    Dog.tag += 1
  
  def get_dog_id(self):
    return str(self.dog_id).zfill(3)
  
  def get_parent_1(self):
    return self.parent1
  
  def get_parent_2(self):
    return self.parent
  
  def speak(self):
    print('woof')
  
  def __str__(self):
    return f"dog:{self.name}:{self.age}"

  def __add__(self, other):
    return Dog(0, self, other)
  

peter = Dog(2)
peter.set_name('Peter')

hopsy = Dog(3)
hopsy.set_name('Hopsy')

cotton = Dog(1, peter, hopsy)
cotton.set_name('Cotton')

print(cotton)
# dog:Cotton:1
print(cotton.get_parent_1())
# dog:Peter:2

mopsy = peter + hopsy
print(mopsy)
# dog:None:0
print(mopsy.get_parent_1())
# dog:Peter:2
print(mopsy.get_parent_2())
# dog:Hopsy:3
```

- `tag` is a class variable -- it is not bound by any instance variable.
- `dog_id` binds the `tag` to it's instance, but increments tag by 1, so next time a `Dog` instance is created, `tag` is going to be 2.
- `tag` used to give **unique id** to each new dog instance

### 5.2. An Extended Example

- Building an application that organizes info about people
- start with a `Person` object
  - Person: name, birthday
    - get last name
    - sort by last name
    - get age

```python
import datetime

class Person(object):

  def __init__(self, name):
    """create a person called name"""
    self.name = name
    self.birthday = None
    self.lastName = name.split(' ')[-1]
  
  def setBirthday(self, month, day, year):
    """sets self's birthday to birthDate"""
    self.birthday = datetime.date(year,month,day)
  
  def getAge(self):
    """returns self's current age in days"""
    if self.birthday == None:
      raise ValueError

    return (datetime.date.today() - self.birthday).days
  
  def getLastName(self):
    """returns self's last name"""
    return self.lastName
  
  def __str__(self):
    """return self's full name"""
    return self.name
  
  def __lt__(self, other):
    """Less Than: returns True if self's name is lexicographically less
        than the other's name, and false otherwise"""
    if self.lastName == other.lastName:
      return self.name < other.name
    
    return self.lastName < other.lastName
  
p1 = Person('Mark Zuckeberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

personList = [p1, p2, p3, p4, p5]

print(p1)
# Mark Zuckeberg

for e in personList:
  print(e)
# Mark Zuckeberg
# Drew Houston
# Bill Gates
# Andrew Gates
# Steve Wozniak

personList.sort()

for e in personList:
  print(e)
# Andrew Gates
# Bill Gates
# Drew Houston
# Steve Wozniak
# Mark Zuckeberg
```

- Expand `Person` info
  - MITPerson: Person + IDNumber
    - assign ID numbers in sequence
    - get ID number
    - sort by ID number

```python
class MITPerson(Person):
  nextIdNum = 0

  def __init__(self,name):
    Person.__init__(self,name)
    self.idNum = MITPerson.nextIdNum
    MITPerson.nextIdNum += 1
  
  def getIdNum(self):
    return self.idNum
  
  def __lt__(self, other):
    return self.idNum < other.idNum
  
  def speak(self, utterance):
    return f"{self.getLastName()} says: {utterance}"
  
m3 = MITPerson('Mark Zuckeberg')
Person.setBirthday(m3,5,14,84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2, 3,4,83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1, 10,28,55)

MITPersonList = [m1, m2, m3]
print(m1)
# Bill Gates
print(m1.speak('Hi there!'))
# Gates says: Hi there!

for e in MITPersonList:
  print(e)
# Bill Gates
# Drew Houston
# Mark Zuckeberg

MITPersonList.sort()

for e in MITPersonList:
  print(e)
# Mark Zuckeberg
# Drew Houston
# Bill Gates
```

- Keep expanding the classes:
  - Students: several types, all MIT Person
    - undergraduate student: has a class year
    - graduate student

```python
class Student(MITPerson):
  pass

class UG(Student):
  def __init__(self, name, classYear):
    MITPerson.__init__(self, name)
    self.year = classYear
  
  def getClass(self):
    return self.year
  
  def speak(self, utterance):
    return MITPerson.speak(self, f"Dude, {utterance}")
  
class Grad(Student):
  pass

class TransferStudent(Student):
  pass

def isStudent(obj):
  return isinstance(obj,Student)

s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad ('Leonardo DiCaprio')

studentList = [s1, s2, s3, s4]

print(s1)
# Matt Damon
print(s1.getClass())
# 2017
print(s1.speak('where is the quiz?'))
print(s2.speak('I have no clue!'))
# Damon says: Dude, where is the quiz?
# Affleck says: Dude, I have no clue!
```

- **Substitution principle:** important behavior of superclass should be supported by all subclasses.
- Inherited methods to leverage methods from other classes in the hierachy
  - Professor class:
    - also MIT Person
    - different behaviors

```python
class Professor(MITPerson):
  def __init__(self, name, department):
    MITPerson.__init__(self, name)
    self.department = department
  
  def speak(self, utterance):
    new = f"In course {self.department} we say "
    return MITPerson.speak(self, new + utterance)
  
  def lecture(self, topic):
    return self.speak(f"it is obvious that {topic}")

faculty = Professor('Doctor Eric Grimsson', 'six')
print(faculty.speak('hi there!'))
# Grimsson says: In course six we say hi there!
print(faculty.lecture('Object Oriented Programming'))
# Grimsson says: In course six we say it is obvious that Object Oriented Programming
```

- Create a class that includes instances of other classes within it
- Concept:
  - build a data structure that can hold grades for students
  - gather together data and procedure for dealing with them in a single structure, so that users can manipulate without having to know internal details

```python
class Grades(object):
  """A mapping from students to a list of grades"""

  def __init__(self):
    """Create an empty grade book"""
    self.students = []
    self.grades = {}
    self.isSorted = True
  
  def addStudent(self, student):
    """Assumes: student is of type Student
       Add student to grade book"""
    if student in self.students:
      raise ValueError('Duplicate student')
    self.students.append(student)
    self.grades[student.getIdNum()] = []
    self.isSorted = False
  
  def addGrade(self, student, grade):
    """Assumes: grade is a float
       Add grade to the list of grades for student"""
    try:
      self.grades[student.getIdNum()].append(grade)
    except KeyError:
      raise ValueError('Student not in grade book')
  
  def getGrades(self, student):
    """Return a list of grades for student"""
    try:
      return self.grades[student.getIdNum()][:]
    except KeyError:
      raise ValueError('Student not in grade book')
  
  def allStudents(self):
    """Return a list of students in the grade book"""
    if not self .isSorted:
      self.students.sort()
      self.isSorted = True
    return self.students[:]

def gradeReport(course):
  """Assumes: course is of type Grades"""
  report = []
  for student in course.allStudents():
    total = 0.0
    numGrades = 0
    for grade in course.getGrades(student):
      total += grade
      numGrades += 1
    try:
      average = total / numGrades
      report.append(f"{student}'s mean grade is {average}")
    except:
      report.append(f"{student} has no grades")
  return '\n'.join(report)

ug1 = UG('Matt Damon',2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)

six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

print(gradeReport(six00))
# Matt Damon's mean grade is 95.0
# Ben Affleck's mean grade is 85.0
# Drew Houston's mean grade is 75.0
# Mark Zuckerberg has no grades
# Bill Gates's mean grade is 100.0
# Steve Wozniak's mean grade is 25.0

six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)
print(gradeReport(six00))
# Matt Damon's mean grade is 87.5
# Ben Affleck's mean grade is 80.0
# Drew Houston's mean grade is 75.0
# Mark Zuckerberg has no grades
# Bill Gates's mean grade is 95.0
# Steve Wozniak's mean grade is 35.0
```

- Current version works but is inefficient: to get a list of all students, we have to create a copy of the internal list
  - Let us manipulate ot without changing the internal structure
  - Works for small, 30-40 students, expensive in a MOOC with hundreds of thousands of students
- **Generators:**
  - Any procedure or method with an `yield` statement is called a **generator**

```python
def genTest():
  yield 1
  yield 2

foo = genTest()
foo.__next__()
# => 1
foo = genTest()
foo.__next__()
# => 2
foo = genTest()
foo.__next__()
# => StopIteration


```

- Generators have a `next()` method wich starts/resumes execution of procedure.
- Inside of generator:
  - `yield` suspend execution and returns a value
  - returning from a generator raises a `StopIteration` exception
- Can use a generator inside a looping structure, as it will continue until it gers a StopIterarion exception:

```python
for n in genTest():
  print(n)

# 1
# 2
```

```python
def genFib():
  fibn_1 = 1 # fib (n - 1)
  fibn_2 = 0 # fib (n - 2)
  
  while True:
    # fib(n) = fib(n - 1) + fib(n - 2)
    next = fibn_1 + fibn_2
    yield next
    # will hold execution until generator called __next__()
    fibn_2 = fibn_1
    fibn_1 = next
    
fib = genFib()
fib.__next__()
# 1
fib.__next__()
# 2
fib.__next__()
# 3
fib.__next__()
# 5
fib.__next__()
# 8
fib.__next__()
# 13
fib.__next__()
# 21
```

- Generators separates the concept of computing a long sequence of objects, from the actual process of computing them explicitly
- allows one to generate each new objects as needed as part of another computation (rather than computing a very long sequence, only to throw most of it away while you do something on an element, then repeating the process)
- have alreary seen this idea in `range`
- Fix to grades class:

```python
def allStudents(self):
    """Return a list of students in the grade book"""
    if not self .isSorted:
      self.students.sort()
      self.isSorted = True
    for student in self.students:
      yield student
```
