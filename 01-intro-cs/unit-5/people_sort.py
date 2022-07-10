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
    return f"{self.name} says: {utterance}"

class Professor(MITPerson):
  def __init__(self, name, department):
    MITPerson.__init__(self, name)
    self.department = department
  
  def speak(self, utterance):
    new = f"In course {self.department} we say "
    return MITPerson.speak(self, new + utterance)
  
  def lecture(self, topic):
    return self.speak(f"it is obvious that {topic}")

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
    for student in self.students:
      yield student

def isStudent(obj):
  return isinstance(obj,Student)

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
print()

for e in personList:
  print(e)
# Mark Zuckeberg
# Drew Houston
# Bill Gates
# Andrew Gates
# Steve Wozniak

personList.sort()
print()

for e in personList:
  print(e)
# Andrew Gates
# Bill Gates
# Drew Houston
# Steve Wozniak
# Mark Zuckeberg

print ('---')

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
print()

for e in MITPersonList:
  print(e)
# Bill Gates
# Drew Houston
# Mark Zuckeberg
print()

MITPersonList.sort()

for e in MITPersonList:
  print(e)
# Mark Zuckeberg
# Drew Houston
# Bill Gates
print('---')

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
print('---')

faculty = Professor('Doctor Eric Grimsson', 'six')
print(faculty.speak('hi there!'))
# Grimsson says: In course six we say hi there!
print(faculty.lecture('Object Oriented Programming'))
# Grimsson says: In course six we say it is obvious that Object Oriented Programming
print('---')

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
print()

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
