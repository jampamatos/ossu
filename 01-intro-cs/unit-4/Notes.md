# INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES

## TABLE OF CONTENTS

- [INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES](#introduction-to-computer-science-and-programming-using-python----notes)
  - [TABLE OF CONTENTS](#table-of-contents)
  - [UNIT 4 - GOOD PROGRAMMING PRACTICES](#unit-4---good-programming-practices)
    - [4.1. Testing and Debugging](#41-testing-and-debugging)
    - [4.2. Exceptions and Assertions](#42-exceptions-and-assertions)

## UNIT 4 - GOOD PROGRAMMING PRACTICES

### 4.1. Testing and Debugging

- **Defensive Programming**: define what to expect from the program and ensure that it will do it
  - Write specifications for functions (doc strings)
  - Modularize programs (break program into small functions)
  - Check conditions on inputs/outputs (assertions)
- **Testing/Validation**:
  - Compare input/output pairs to specification
  - "How can I break my program?"
- **Debugging**:
  - Study events leading up to an error
  - "How can I fix my program?"
  
- **Set yourself up for easy testing and debugging!**
  - Design code that ease test and debug by building self-contained modules that can be tested inividually
  - build doc strings, document modules, functions, assumptions on code...

- to test:
  - ensure code runs
    - remove syntax errors
    - remove static semantic errors
  - have a set of expected results
    - an input set
    - for each input, expected output

- **Classes of tests:**
  - *Unit Testing:*
    - validade each piece of program
    - test each function separately
  - *Regression testing:*
    - Add test for bugs as you find them in a function
    - catch reintroduced errors that were previously fixed
  - *Integration Testing:*
    - test overall program
    - programmers tend to rush to do this

- Testing approaches:
  - intuition about natural boundaries to the problem
    - if you can't find natural partitions, do random testing -- the more we test, the better the changes of code working correctly
  - *black box testing*:
    - never look at the code, only look at the spec
    - if done by someone other than the implementer might help aboid biases
    - can be reused if implementatio changes
    - build test cases in different natural space partitions (empty list, list of one, list of many, small numbers, large numbers, etc)
  - *glass box testing:*
    - use code directly to guide design of test cases
    - **path-complete** if every potential path through the code is tested at least once
    - **drawbacks**:
      - can go through loops arbitrarily many times
      - missing paths
    - guidelines:
      - branches
      - for loops
      - while loops

- **Bugs**
  - once the code doesn't run:
    - isolate bugs
    - erradicate bugs
    - retest until code runs correctly
  - Runtime bugs:
    - *Overt bugs:* has an obvious manifestation - code crashes or runs forever
    - *Covert bugs:* no obvious manifestation - return an incorrect value but hard to determine
    - *Persistent bugs:* occurs every time code is run
    - *Intermitent bugs:* only occurs some times, even if run on same input

- **Debugging**
  - steep learning curve
  - goal is to have a bug-free program
  - tools:
    - built into IDE
    - Python Tutor
    - `print` statement
    - be *systematic* in your hunt
  - `print` statemens to test hypothesis:
    - print when enter a function
    - print values of the parameters
    - print function results
    - bisection method:
      - put priny halfway in the code
      - decide where bug might be depending on values
  - Debugging steps:
    - **study** program code:
      - ask how did I get the unexpected result
      - don't ask what is wrong
      - is it part of a family?
    - **scientific method:**
      - study available data
      - form hypothesis
      - repeatable experiments
      - pick simplest input to test with

### 4.2. Exceptions and Assertions

- Execptions deal with when execution hits an unexpected condition - an **error**
- What happens?
  - **fail silently:**
    - substitute default value or just continue
    - bad idea because user gets no warning
  - return an **error value**
    - what value to choose
    - complicates code having to check for a special value
  - stop execution, **signal error** condition:
    - raise an **exception*
    - `raise Exception("descriptive string")`
- Python code can provide handlers for exceptions:

```python
try:
  a = int(input("Tell me one number: ")
  b = int(input("Tell me another number: ")
  print (a/b)
  print("Okay")
except:
  print("Bug in user input.")
print("Outside")
```

- Exceptions examples:

```python
while True:
  try:
    n = int(input("Please enter an integer: "))
    break
  except ValueError:
    print("Input not an intefer; try again")
print("Correct input of an integer!")
```

- Controling input:

```python
data =[]
file_name = input("Provide a name of a file of data: ")

try:
  fh = open(file_name, 'r')
except IOError:
  print("cannot open", file_name)
else:
  for new in fh:
    if new != '\n':
      addIt = new[:-1].split(',') # remove trailing \n
      data.append(addIt)
      fh.close() # close file even if fail

gradesData = []

if data:
  for student in data:
    try:
      name = student[0:-1]
      grades = int(student[-1])
      gradesData.append([name,[grades]])
    except ValueError:
      gradesData.append([student[:],[]])
```

- Raising an exception

```python
def get_ratios(L1, L2):
  
  ratios = []
  for index in range(len(L1)):
    try:
      ratios.append(L1[index]/float(L2[index]))
    except ZeroDivisionError:
      ratios.append(float('NaN'))
    except:
      raise ValueError('get_ratios called with bad arg')
  return ratios
```
