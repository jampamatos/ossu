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
    - int;
    - float;
    - bool;
    - NoneType (None);

  - **non-scalar** (have internal structure that can be accessed):

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

&nbsp;

- **equality** is done with `==`; **inequality** with `!=`

- logic operators on bools:
  - `and;
  - or;
  - not`

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
