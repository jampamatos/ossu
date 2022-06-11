# INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES

## TABLE OF CONTENTS

- [INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES](#introduction-to-computer-science-and-programming-using-python----notes)
  - [TABLE OF CONTENTS](#table-of-contents)
  - [UNIT 1 - PYTHON BASICS](#unit-1---python-basics)
    - [1.1. Introduction to Python](#11-introduction-to-python)
    - [1.2. Core Elements of Programs](#12-core-elements-of-programs)

## UNIT 1 - PYTHON BASICS

### 1.1. Introduction to Python

- **DECLARATIVE KNOWLEDGE:** statements of fact, no details about it.
  - square root of `x` is `y` such as `y * y = x`.

- **IMPERATIVE KNOWLEDGE:** recipe, a 'how to' information, sequence of steps to find a solution
  1. start with a guess `g`;
  2. if `g * g` is close enough to `x`, stop and say `g` is the answer;
  3. otherwise make a new guess by averaging `g` and `x / q`;
  4. repeat until close enough.

- **RECIPE** is an ALGORITHM:
  1. sequence of simple steps;
  2. flow control that specified when nex step is executed;
  3. mean to determining when to stop

- Types of machines to capture a recipe in mechanical process:
  
1. **fixed program computer:** design specifically to solve a problem (calculator)
2. **stored program:** load sequence of instructions in that computer, by an interpreter that will simulate a fixed program computer for each program loaded into it

- **Basic Machine Architecture**:
  - *Memory* - data or instructions;
  - *Input*;
  - *Output*;
  - *Arithmetic Logic Unit (ALU)* - takes info from memory, reads it in, do a primitive operation (add, subtract), store stuff back into memory
  - *Control Unit* - keep track of what operation to do in the ALU, and a program counter that points to the location of the intructions

- in the Stored Program Computer an interpreter (special program) executes each instruction in order, use tests to change flow of control through sequence and stop when done.

- >*Turing*: "You can compute anything with 6 primitives"

  1. move left
  2. move right
  3. scan
  4. read
  5. write
  6. do nothing

- modern programming languages have more convenient set of primitives
- can abstract methods to **create new primitives**

- anything computable in one language is computable in any other programming language : **TURING COMPLETE**

- expression are complex but legal combinations of primitives in a programming language

- programming primitives:
  
1. number
2. strings
3. simple operators

- **programming sytax:** parsing of a combination of primitives, legal and valid for that language

- **programming static semantics:** in which syntactically valid strings have meaning (`3 + "hi"` is syntactically valid but with a stactic semantic error)

- **programming semantics:** a code of line that can be semantically correct but deliveing an incorrect result ('bugs')

- a program is a sequence of definitions (*evaluated*) and commands (*executed*)

- object has a type that defines the king of things programs can do
- we can cast a type of object into another (convert)
  
  - **scalar (cannot be subdivided)**:
    - `int`;
    - `float`;
    - `bool`;
    - `NoneType` (None);

  - **non-scalar** (have internal structure that can be accessed):
    - `string`;

- expression: `<object> <operator> <object>`

- operator precedence:

  1. parenthesis first
  2. `**`
  3. `*`
  4. `/`
  5. `+` and `-`
  6. left to right as appear in expression

&nbsp;

- a *variable* can be assigned by an equal sign, in which will store it in computer memory, binding a value to a name allowing its value to be retrieved by invoking it.
  
- variables allows us to reuse names instead of value, makes code easier to change and read.

- cannot be keywords

- swap variables:

```python
x = 1
y = 2

y = x
x = y
# Won't work, x and y will be 1
```

```python
x = 1
y = 2

temp = y # Bind y value to a temporary variable
y = x
x = temp # Bind the temp value -- which was y's -- to x.
```

```python
# Using a tupple
x = 1
y = 2

y,x = x,y
# Python is unpacking the tuple on the right side of the = and storing it to the variable names on the left side. 
```

&nbsp;

- Comparing **equality** is done with `==`; **inequality** with `!=`

- logic operators on bools:
  - `and`;
  - `or`;
  - `not`

- branching program:
  - a test that evaluates True of False
  - a block of code to exectute if True;
  - an optional block of code to execute if False

```python
x = int (input('Enter an ingeger: '))

if x % 2 == 0  # Test
 print ('') #True Block
 print('Even')

else:
 print('') #False Block
 print('Odd')
 
print ('Done with conditional')
```

- Indetation express the block of code

- **Nested conditionals:**

```python
if x % 2 == 0:

 if x % 3 == 0:
  print ('Divisible by 2 and 3')

 else:
  print ('Divisible by 2 and not by 3')

elif x % 3 == 0:
 print( 'Divisible by 3 and not by 2')
```

- **Compound booleans**:

```python
if x < y and x < z:
 print ('x is least')

elif y < z:
 print ('y is least')

else:
 print ('z is least')
```

- Branching programs are linear programs because they run in constant time and execute each instruction at most once
- The maximum time to run the program depends on the length of the program

### 1.2. Core Elements of Programs

- String:
  - letters, special charactes, spaces, digits
  - enclosd in double or single quotation mark
  - string concatenation is done with `+`.
  - the type of an object tell the operator what to do: `+` with `int`will add numbers, `+`with `string`will concatenade **-- OVERLOAD**

  - operations on strings:
    - `'ab' + 'cd'` **- concatenation**
    - `3 * 'eric'` **- successive concatenation**
    - `len('eric')` **- length**
    - `'eric'[1]` **- indexing**
    - `'eric'[1:3]` **- slicing**:

```python
'eric'[1:3]
# returns 'ri'
'eric'[:3]
#returns 'eri'
'eric'[1:]
# returns 'ric'
'eric'[:]
#returns 'eric'
```

- String slicing with negative indices:

```python
str = 'Hello, World!'
str[-11:-5] #start at -5, until, but not including, -11
# returns 'llo, W'
str[-5:-11:-1] # Negative step, inverts the order of scan
# returns 'oW, ol'
str [-5:]
# returns 'orld!'
str [: -9]
# returns 'Hell'
str[::-2] # Negative step
# returns '!lo olH'
```

- Comparing strings:
  - comparison uses **lexicographical ordering**:
    1. first the two items are compared, and if they differ this determines the outcome of the comparison;
    2. if they are equal, the next two are compared, and so on
    3. if all items are equal, the sequence is considered equal

`'ABCDI' > 'ABCDA'`

1. `'A' == 'A' True`
2. `'B' == 'B' True`
3. `'C' == 'C' True`
4. `'D' == 'D' True`
5. `'I' == 'A' False`
6. `'I' > 'A' True`
7. Then `'ABCDI' > 'ABCDA'` is `True`

- Lexicographical order is the Unicode code point number of a char (function `ord()`)
- Unicode code for uppercase and lowercase letter are **NOT THE SAME**:

```python
ord('a')
# returns 97
ord ('A')
# returns 65
'A' > 'a'
# returns False
'A' == 'a'
# returns False
'A' < 'a'
# returns True
```

- The Pyton `in` Operator:
  - The operators `in` and `not in` test for a collection membership, as in `element in coll` will return `True` if that element is in that collection, and `False` otherwise.

- Input/Output:
  - `print` output stuff to console
  - `print` with multiple arguments will print each one spaced apart, but concatenated they will be joined together.

  - `input('str')` will print `str` parameters and wait for user input, then return the entered sequence **as a string**.
  - should be binded to a variable

&nbsp;

- Control in Loops:
  - control the flow in a non-linear way

- `while` loop:

```python
while <condition>
  <expression>
  <expression>
  ...
```

1. `<condition>` evaluates to a Boolean
2. if `<condition>` is `True`, do all the steps in the code block.
3. check `<condition>` again.
4. repeat until `<condition>` is `False`.

```python
n = 0
while (n < 5):
  print(n)
  n += 1
```

&nbsp;

- `for` loop:

```python
for <variable> in range(<some_num>):
  <expression>
  <expression>
  ...
```

1. each time through the loop, `<variable>` takes a value
2. first time, `<variable>` starts at the smallest value
3. next time, `<variable>` gets prev value + 1
4. runs block of code at each iteration, until range ends.

```python
for n in range(5):
  print(n)
# >> 0
# >> 1
# >> 2
# >> 3
# >> 4
# range(int) returns a sequence of integers starting at 0 and ending before 'int'.
```

- `range(start, stop, step)`:
  - default values are `start = 0` and `step = 1` and are optional
  - loop until value is `stop - 1`.

```python
mysum = 0
for i in range (7,10):
  mysum += i
print(mysum)
# >> 24
# 7, 8 and 9 added together.
```

```python
mysum = 0
for i in range (5,11,2):
  mysum += i
print(mysum)
# >> 21
# 5, 7 and 9 added together
```

- `break` statement
  - immediately breaks out of loop, skipping remaining expressions in code block (*only innermost loop*).

```python
while <condition_1>:
  while <condition_2>:
    <expression_a>
    break
    <expression_b> #will never execute this expression
  <expression_c>
```

```python
mysum = 0

for i in range(5,11,2):
  mysum += i
  if mysum == 5:
    break
print(mysum)
# >> 5
```

| for loops                                          | while loops                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------------------|
| **known** number of iterations                     | **unbounded** number of iterations                                                  |
| can **end early** via `break`                      | can **end early** via `break`                                                       |
| uses a **counter**                                 | can use counter but **must be initialized** before loop and incremented inside loop |
| **can rewrite** a `for` loop using a `while` loop  | **may not be able** to rewrite a `while` loop using a `for` loop                    |

- Truthy and falsy values:

```python
num = 5

if num:
  print('Yes')
else:
  print ('No')

# Will print 'Yes'.
```

```python
str = '123'

if string:
  print('Hi')
else:
  print('Bye')

# Will print 'Hi'.
```

- a **truthy** value is a value that is considered `True` when evaluated in a Boolean context.
- a **falsy** value is a value that translates `False` when evaluated in a Boolean context.

| Truthy | Falsy |
|--------|-------|
| Any number that is **NOT** 0 (positive and negative) | The number 0
| Any string **NOT EMPTY** | An empty string `''` or `""`|
|   | `None`

- Iteration:
  1. Start with a `Test`
  2. If evaluates to `True`, then execute loop body once, and go back to reevaluate the `Test`
  3. Repeat until `Test` evaluates to `False`, after which code following iteration statement is executed.

Example: **square of a number by repetitive addition**

`n² = n + n + n +... n` repeated `n` times.

```python
x = 3
ans = 0
itersLeft = x

while (itersLeft != 0):
  ans = ans + x
  itersLeft -= 1

print(str(x) + '*' + str(x) + ' = ' + str(ans))

# >> 3*3 = 9
```

- Guess and check methods technique:
  - Finding cube root of integer:
  - Only positive integers:

```python
x = int(input('Enter an integer: '))
ans = 0

while ans**3 < x:
    ans = ans + 1

if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of '+ str(x) + ' is ' + str(ans))
```

- To also test negative integers:

```python
x = int(input('Enter an integer: '))
ans = 0

while ans**3 < abs(x): # takes the absolute value of x
    ans = ans + 1

if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of '+ str(x) + ' is ' + str(ans))
```

- In a for loop:

```python
x = int(input('Enter an integer: '))

for guess in range(abs(x) + 1):
    if guess**3 >= abs(x):
        break

if guess**3 != abs(x):
    print(x, 'is not a perfect cube.')
else:
    if x < 0:
        guess = -guess 
    print ('Cube root of ' + str(x) + ' is ' + str(guess))
```
