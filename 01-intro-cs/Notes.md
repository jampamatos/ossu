# INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES

## TABLE OF CONTENTS

- [INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES](#introduction-to-computer-science-and-programming-using-python----notes)
  - [TABLE OF CONTENTS](#table-of-contents)
  - [UNIT 2 - SIMPLE PROGRAMS](#unit-2---simple-programs)
    - [2.1. Simple Algorithms](#21-simple-algorithms)

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
