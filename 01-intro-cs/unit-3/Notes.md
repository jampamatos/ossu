# INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES

## TABLE OF CONTENTS

- [INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES](#introduction-to-computer-science-and-programming-using-python----notes)
  - [TABLE OF CONTENTS](#table-of-contents)
  - [UNIT 3 - STRUCTURED DATA TYPES](#unit-3---structured-data-types)
    - [3.1. Tuples and Lists](#31-tuples-and-lists)
    - [3.2. Dictionaries](#32-dictionaries)

## UNIT 3 - STRUCTURED DATA TYPES

### 3.1. Tuples and Lists

- **Tuples:**
  - ordered sequence of elements, can mix element types
  - ordered not because the elements are in order, but because the sequence itself has an order
  - this means I can index different parts of a sequence and access them
  - tuples are **immutable**, we can't change their inner pieces
  - tuples are designate by the parenthesis `()`

```python
te = () #creates an empty tuple

t = (2, 'one', 3) #creates a tuple with three elements

t
# >> *2, 'one', 3)

t[0]
# >> 2

t + (5,6)
# >> (2, 'one', 3, 5, 6)

t[1] = 4
# TypeError: 'tuple' object does not support item assignment

t[1:2]
# >> ('one',)
# The extra comma tells me this is a tupple

f = ('one',)
# >> ('one',)
# Creates a tuple with only one element

g = ('one')
# >> 'one'
# Python treats the parenthesis as if they're scoping the element, and do not create a tuple
```

- convenient to *swap variables*

```python
temp = x
x = y
y = temp
```

```python
(x,y) = (y,x)
```

- return *more than one* value from a function

```python
def quotient_and_remainder(x,y):
    q = x//y
    r = x % y
    return (q,r)

(quot, rem) = quotient and remainder(4,5)
```

- tuples are *iterable*

```python
def get_data(aTuple):
    num = ()
    words = ()

    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)
```

- **Lists:**
  - also ordered sequence of information, also accessible by index
  - denoted by *square brackets*, `[]`
  - a list contain *elements*:
    - usually homonegeous (i.e., all integers)
    - can contain mixed types
  - list elements can be changed so a list is **mutable**
  - also indexed with indices starting at 0

```python
a_list = [] #creates empty list
b_list = [2, 'a', 4, True]

L = [2, 1, 3]

len(L)
# >> 3

L[0]
# >> 2

L[2] + 1
# >> 4

L[3]
# Index error

L[1] = 5
# >> [2, 5, 3]
```

- **Operations on lists - Add:**
  - add elements to the end of list with `L.append(element)`
  - this **mutates** the list itself

```python
L = [2, 1, 3]
L.append(5)
L
# >> [2, 1, 3, 5]
```

- to combine list together use **concatenation** with the operator `+`

```python
L1 = [2, 1, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
L3
# >> [2, 1, 3, 4, 5, 6]
```

- **mutate** the list with `L.extend(some_list)`

```python
L1 = [2, 1, 3]
L1.extend([0,6])
L1
# >> [2, 1, 3, 0, 6]
```

- **Remove itens from list**
  - delete elements at a specific index with `del(L[index])`
  - remove last element of a list by popping it with `L.pop()`, changes the list itself and return the removed element
  - remove a specific element with `L.remove(element)`
    - looks for element in list
    - if one found, remove it
    - if multiple elements in list, removes only the first
    - if element not in list, gives an error

```python
L = [2, 1, 3, 6, 3, 7, 0]

L.remove(2)
# >> [1, 3, 6, 3, 7, 0]

L.remove(3)
# >> [1, 6, 3, 7, 0]

del(L[1])
# >> [1, 3, 7, 0]

L.pop()
# >> 0

L
# >> [1, 3, 7] 
```

- **Convert lists to strings and back**
  - convert *string to list* with `list(s)`, returns a list with every character from `s` an element in `L`
  - `s.split()` will **split a string on a character** parameter, splits on spaces if called without a parameter
  - use `''.join(L)` to turn a **list of characters into a string**, can give a character in quotes to add char between every element
  
 ```python
 s = "I <3 cs"
 
 list(s)
 # >> ['I', ' ', '<', '3', ' ', 'c', 's']
 
 s.split('<')
 # >> ['I ', '3 cs']
 
 L = ['a', 'b', 'c']
 ''.join(L)
 # >> 'abc'
 
 '_'.join(L)
 # >> 'a_b_c'
 ```

- **Other list operations**
- `sort()` and `sorted()`
- `reverse()`

```python
L = [9, 6, 0, 3]

sorted(L)
# >> [0, 3, 6, 9]
# DOES NOT MUTATE THE LIST!!!

L.sort()
# >> [0, 3, 6, 9]
# MUTATES THE LIST!!!

L.reverse()
# >> [9, 6, 3, 0]
# MUTATES THE LIST
```

- Lists are mutable, thus behaving differently than immutable types
- A list is an object in memory with a variable that points to it
- We can have multiple variables poiting to a list -- making them **same instance** but with different names -- **aliases**
- If one element is changed in one of the variable names, it changes to all variable names

```python
warm = ['red', 'yellow', 'orange']
hot = warm

# hot is an ALIAS for warm -- changing one changes both

warm
# >> ['red', 'yellow', 'orange']
hot
# >> ['red', 'yellow', 'orange']

hot.append('pink')

hot
# >> ['red', 'yellow', 'orange', 'pink']
warm
# >> ['red', 'yellow', 'orange', 'pink']
```

- **Print is not the same**
  - if two lists print the same thing, does not mean they are the same structure
  - can test by mutating one, and checking

```python
cool = ['blue', 'green', 'grey']
chill = ['blue', 'green', 'grey']

print(cool)
# >> ['blue', 'green', 'grey']
print(chill)
# >> ['blue', 'green', 'grey']

chill[2] = 'blue'

print(cool)
# >> ['blue', 'green', 'grey']
print(chill)
# >> ['blue', 'green', 'blue']
```

- Cloning a list
  - create a new list and **copy every element** usint `listA = listB[:]`
  
```python
cool = ['blue', 'green', 'grey']
chill = cool[:]

chill.append('black')
print(chill)
# >> ['blue', 'green', 'grey', 'black']
print(cool)
# >> ['blue', 'green', 'grey']
```

- in nested lists, changing one list changes the nested list as well

```python
warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]

print(brightcolors)
# >> [['yellow', 'orange']]

brightcolors.append(hot)
print(brightcolors)
# >> [['yellow', 'orange'], ['red']]

hot.append('pink')
print(hot)
# >> ['red', 'pink']
print(brightcolors)
# >> [['yellow', 'orange'], ['red', 'pink']]

print(hot+warm)
# >> ['red', 'pink', 'yellow', 'orange']
```

- Mutation and iteration
  - **avoid** mutating lists as you are iterating over it

```python
def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [1,2,3,4]
L2 = [1,2,5,6]

remove_dups(L1, L2)
L1
# >> [2, 3, 4]
```

- The code abode **does not** remove `2`because Python, because it's going over an iterable, uses as internal counter to keep track of index in its loop
- When I mutate the list, it changes it, so python never sees the element 2, because it changes the size of the list
- To fix it, make a **copy**

```python
def remove_dups(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
    # The list will iterate over the copy

L1 = [1,2,3,4]
L2 = [1,2,5,6]

remove_dups(L1, L2)
L1
# >> [2, 3, 4]
```

- **Functions as objects**
  - functions are **first class objects*:
    - have types
    - can be elements of data structures like lists
    - can appear in expressions
      - as part of an assignment statement
      - as an argument to a function
  - particulary useful to use functions as arguments when coupled with lists aka **higher order programing**

```python
def applyToEach(L, f):
    """
    assumes L is a list, f a function
    mutates L by replacing each element, e, of L by f(e)
    """

    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.4]

applyToEach(L, abs)
# >> [1, 2, 3.4]

applyToEach(L, int)
# >> [1, 2, 3]

applyToEach(L, fact)
# >> [1, 2, 6]

applyToEach(L, fib)
# >> [1, 2, 13]
```

```python
def applyFuns(L, x):
    for f in L:
        print(f(x))

applyFuns([abs, int, fact, fib], 4)
# 4
# 4
# 24
# 5
```

- Generalization of Higher Order Procedure - `map`
  - it takes a function that expects only one parameter, takes a list of appropriate arguments and creates a list where the function is applied to each element in turn
  - it returns an iterable object so need to walk down it

```python
for elt in map(abs, [1, -2, 3, -4]:
  print(elt)
# >> [1, 2, 3, 4]
```

- general form - an n-ary function and n collections of arguments

```python
L1 = [1, 28, 36]
L2 = [2, 57, 9]

for elt in map(min, L1, L2):
    print(elt)

# >> [1, 28, 9]
# prints the minimum of the two lists at each place
```

### 3.2. Dictionaries
