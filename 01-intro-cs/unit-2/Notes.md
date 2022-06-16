# INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES

## TABLE OF CONTENTS

- [INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES](#introduction-to-computer-science-and-programming-using-python----notes)
  - [TABLE OF CONTENTS](#table-of-contents)
  - [UNIT 2 - SIMPLE PROGRAMS](#unit-2---simple-programs)
    - [2.1. Simple Algorithms](#21-simple-algorithms)
    - [2.2. Simple Programs](#22-simple-programs)

## UNIT 2 - SIMPLE PROGRAMS

### 2.1. Simple Algorithms

- Strings:
  - sequence of case sensitive characters
  - compare with compare operators, `len`() for length
  - slicing strings with `[start:stop:step]`
  - negative step access string in reverse order
  - strings are **immutable** and cannot be changed -- have to be redefined

```python
s = 'hello'
print(s[0])
# >> 'h'

s[0] = 'y'
# TypeError: 'str' object does ot support item assignment

s = 'y' + s[1:]
print(s)
# >> 'yello'
```

- `for`loop can loop through strings -- they are **ITERABLE**

```python
s = 'abcdefgh'

for index in range(len(s)):
  if s[index] == 'i' or s[index] == 'u':
    print("There is an i or u")
```

```python
s = 'abcdefgh'

for char in s:
  if char == 'i' or char == 'u':
    print("There is an i or u")
```

- Aproximate solutions:

1. start with a guess (such as `1`)
2. check if it is close enough
3. if it is not, increment by a small value (such as `1.001`)
4. define how close is close enough: `|guess³| - cube <= epsilon (less or equal a small number)

- if we decrease increment size we get better results but with a slower program
- similarily when we increase epsilon we might have a faster program but with a less accurate answer

```python
cube = 10
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)

if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube roof of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
```

- step could be any small number
  - if too small, takes a long time to find square root
  - if too large, might skip over answer withou getting close enough
- in general, will take x/step times through code to find sollution **- inneficient**.

&nbsp;

- **Biscetion Search:**
- to find square root of x:

1. pick a number (`g`) in the middle of `range(1:x)`
2. If close enough, stop, if not ask if `g` is too big or too small
3. If `g² > x`, `g`is too big, so the new number, `h`, will be in the middle of `range(1:g)`
4. If now `h` is such that `h² < x`, `h`is too small, so new number, `i`, will be in the middle of `range(g,h)
5. repeat until finding the solution.

```python
x = 25
epsilon = 0.01
num_guesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    num_guesses += 1
    if ans**2 < x: 
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('Number of guesses:', num_guesses)
print(str(ans) + 'is close to square root of ' + str(x))
```

- this code only works with integers. to work with fractions, search space:
  - rather going from 1 to x, it goes from x to 1
- bisection search works when value of function varies monotonically with input
- fast: it's a logarithmic time algorithm
- should work well on problems with ordering property -- that is, the value of function being solved varies monotonically with input value
  - `g²` grows as `g` itself grows

- **Floats:**
  - decimal 302: `3*10² + 0*10¹ + 2*10⁰`
  - binary number 10011 = 1*2⁴ + 0*2³ + 0*2² + 1*2¹ + 1*2⁰ which in decimals is 16 + 2 + 1 = 19)

- Internally, computer represents numbers in binaries

- convertin decimal integer to binary:
  - x = 1*2⁴ + 0*2³ + 0*2² + 1*2¹ + 1*2⁰ = 10011

1. Take the remainder relative to 2 (`x%2`) to get the last binary bit
2. Divide x by 2 (`x//2`) to get all bits shifted right `x//2 = 1*2³ + 0*2² * 0+2¹ + 1*2⁰ = 1001`
3. Keep doing successives divisions; now remainder gets next bit and so on

```python
num = 19
result = ''

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result
    num = num // 2

if isNeg:
    result = '-' + result

print(result)
```

- with fractions:
  - 3/8 = 0.375 = 3*10⁻¹ + 7*10⁻² + 5*10⁻³
  - if we multiply by a power of two big enough to convert into a whole number, can then convert to binary then divide by same power of 2
  - 0.375 * 2³ = 3 (decimal)
  - convert 3 to binary (11)
  - 11/2³ = 0.011 (binary) - shift right three points

```python
x = .375
p = 0

while ((2**p)*x) % 1 != 0:
    print('Remainder = ' + str((2**p) * x - int ((2**p) * x)))
    p += 1

num = int (x*(2**p))
result = ''

if num == 0:
    result = '0'

while num > 0:
    result = str(num%2) + result
    num = num // 2

for i in range (p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))
```

- if there is no `int p` such that `x * (2**p)` is a wjole number, the binary representation will be an approximation
- testing equality of floats in not exact:
  - suggest `abs(x-y) > small_num` rather than `x==y`

&nbsp;

- **Newton-Raphson:**

- General approximation algorithm to find roots of a polynomial in one variable
- To find the square root of 24 `p(x) = x² - 24`
- If `g`is an approximation to the root, then `g - p(g)/p'(g)` is a better approximation; where p' is the derivative of p
- If a polynomial is x² + k, the derivative is 2x
- In Newton-Raphson: `g - (g² - k)/2g`

```python
epsilon = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess ** 2) - y) / (2*guess))

print('numGuesses =', numGuesses)
print('Square root of', y, 'is', guess)
```

### 2.2. Simple Programs

- one file with one computation, with some piece of code containing a sequence of instructions is fine for small scale problems, but can get messy for larger problems
- need a way to structure program
- Good Programing:
  - more code not necessarily a good thing
  - measure good programmers by the amount of functionality
  - decomposition and abstraction

- **function -** a way to encapsulate pieces of computation
- **decomposition -** break problem into different, self-contained, pieces
- **abstraction -** suppress details of method to compute something from use of that computation

- in programming, to decomposite a code is to divide it into **modules**
  - self-contained
  - reusable
  - organized
  - coherent
- in programming, **abstraction** means to think of a piece of code as a *black box*
  - cannot see details
  - don't need to see details
  - hide tedious coding details
  - **function specifications** and **docstrings**

- functions won't be computed unil invoked.
- function characteristics:
  - has a name
  - has parameters (0 or more)
  - has a docstring (optional but recomended)
  - has a body -- sequence of instructions to happen when the function is called

```python
def is_even(i):
    """
    DOCSTRING:
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """

    print("Hi!")
    return i%2 == 0

is_even(3)
```

- keyword `return` stops the computation and the value of the following expression is the one that will be returned to whatever called that function

- variable scope:
  - formal parameters gets bound to the value of the actual parameter when function is called
  - new scope is created when enter a function
- if a function has no `return` statement, it `return`s as `None`

| `return`                                                       | `print`                                                   |
|----------------------------------------------------------------|-----------------------------------------------------------|
| only has meaning **inside** of function                        | can be used **outside** of function                       |
| only **one** `return` executed inside of function              | can execute **many** `print` statements inside a function |
| code inside function but after `return` statement not executed | code can be executed after `print` statement              |
| has value associated to it, **given to function caller**       | has value associated to it, **outputted to console**      |

- inside a function, **can access** a variable defined outside
- inside a function, **cannot modify** a variable defined outside

```python
def f(y):
    x = 1
    x += 1
    print(x)

x = 5
f(x)
print(x)

# >> 2
# >> 5
# x is redefined in scope of f, but different x objects are print
#the first one from inside the function, the second one the global defined.
```

```python
def g(y):
    print(x)
    print(x+1)

x = 5
g(x)
print(x)

# >> 5
# >> 6
# >> 5
# g gets the value of x from outside, but the last print shows the global defined x.
```

```python
def h(y):
    x = x + 1

x = 5
h(x)
print(x)

# UnboundLocalError: local variable 'x' referenced before assignment
```

- Keyword arguments and default values:

```python
def printName(firstName, lastName, reverse):
  if reverse:
    print(lastName + ', ' + firstName)
  else:
    print(firstName + ', ' + lastName)

printName("Jampa", "Matos", True)
# >> Matos, Jampa
printName("Jampa", "Matos", False)
#>> Jampa, Matos
```

```python
def printName(firstName, lastName, reverse = False):
  if reverse:
    print(lastName + ', ' + firstName)
  else:
    print(firstName + ', ' + lastName)

printName("Jampa", "Matos", True)
# >> Matos, Jampa
printName("Jampa", "Matos")
#>> Jampa, Matos

# The default value for reverse is set to False, so if we omit it, it will be False. It will only be True if we explicitly tells it.
```

- Specifications:
  - a contract between the implementer of function and users
  - **Assumptions:** conditions that must be met by clients -- values of parameters
  - **Guarantees:** conditions that must be met by the function, providing it has been called in manner consistent with assumptions.
  - to be put in a **docstring**

```python
def is_even(i):

  """
  Input: i, a positive integer
  Returns True if i is even, otherwise False
  """
  
  print ('hi')
  return i % 2 == 0
```

- **Iteration** *vs* **Recursion**
- Recursion is a way to design solutions by breaking up into pieces that are reusable -- **divide and conquer**
- A function that inside of its body it calls itself

- **Iterative algorithms** are looping constructs (`while` or `for` loops) with a set of variables that update each time through the loop.

```python
# An iterative solution to a function that multiplies 'a' by 'b' by adding 'a' to itself 'b' times

def mult_inter(a,b):
  result = 0
  while b > 0:    # iteration
    result += a   # current value of computation
    b -= 1        # current value of iteration variable
  return result
```

- In a recursive solution, you will have to reduce problem to a simple/smaller version of the same problem
- you have to find a **base case**, which is a simple case that can be solved directly:

`a * b = b * (a + a + a + a... + a)`

`a * b = a + (b-1 * (a + a + a + ...a))`

`a * b = a + a + (b-2 * (a + a + ...a))`

when b = 1, a * b = a, so:

```python
def mult(a, b): 

  if b == 1:                  #base case
    return a
  else:
    return a + mult(a, b-1)   #recursive step
```

- Factorial:

```python
def factorial (n):
  if n == 1:
    return 1
  else:
    return n * factorial (n-1)
```

- Towers of Hanoi problem recursively:

```python
def printMove(fr, to):
    print('Move from', fr, 'to', to)

def towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)

print(towers(4, 'P1', 'P2', 'P3'))
```

- Fibonacci numbers:

```python
def fib(x):
    '''
    Assumes x and int >= 0
    Returns Fibonacci sum of x
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
```

- Palindromes:

```python
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    
    return isPal(toChars(s))
```

- **Divide and conquer:** solving a hard problem by breaking it into a set of sub-problems such that:
  - sub-problems are easier to solve than the original
  - solutions of the sub-problems can be combined to solve the original

- Modules and files:
  - so far all code stored in one file
  - large collection of code should use different files -- **modules** -- which are .py files containing collections of Python definitions and statements

```python
# a file called 'circle.py'

pi = 3.14159

def area(radius):
  return pi * (radius ** 2)

def circumference(radius):
  return 2 * pi * radius
```

```python
import circle

pi = 4

print(pi)
#>> 3

print(circle.pi)
#>> 3.14159

print(circle.area(3))
#>> 28.27431

print(circle.circumference(3))
#>> 18.849539999999998
```

- If we don't want to refer to functions and variables by their module, we can use:

```python
from circle import *

print(pi)
#>> 3.14159

print(area(3))
#>> 28.27431
```

- **Files**:
  - need a way to save our work for later user
  - operating systems have their own way of handling files -- Python uses a **file handler** that access files operating-system independent
  - `nameHandle = open('kids', 'w')` creates a file named `kids` and returns a file handler which we can name and reference
  - the `w` indicates the file is opened for writing into it.

```python
nameHandle = open('kids', 'w')

for i in range(2):
  name = input('Enter name:')
  nameHandle.write(name + " \ ") #'Enter' key
nameHandle.close() 
```

```python
nameHanle = open('kids', 'r')
for line in nameHandle:
  print(line)
nameHandle.close()
```
