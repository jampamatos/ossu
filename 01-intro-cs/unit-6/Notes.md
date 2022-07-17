# INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES

## TABLE OF CONTENTS

- [INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES](#introduction-to-computer-science-and-programming-using-python----notes)
  - [TABLE OF CONTENTS](#table-of-contents)
  - [UNIT 6 - ALGORITHMIC COMPLEXITY](#unit-6---algorithmic-complexity)
    - [6.1. Computational Complexity](#61-computational-complexity)
      - [6.1.1. Program Efficiency](#611-program-efficiency)
      - [6.1.2. Big Oh Notation](#612-big-oh-notation)
      - [6.1.3. Complexity Classes](#613-complexity-classes)
      - [6.1.4. Recursion Complexity](#614-recursion-complexity)
      - [6.1.4. Big Oh Summary](#614-big-oh-summary)
    - [6.2. Searching and Sorting Algorithms](#62-searching-and-sorting-algorithms)
      - [6.2.1. Search Algorithms](#621-search-algorithms)
      - [6.2.2. Bisection Search](#622-bisection-search)

## UNIT 6 - ALGORITHMIC COMPLEXITY

### 6.1. Computational Complexity

#### 6.1.1. Program Efficiency

- If computers are fast, is program efficiency really important?
  - data sets can be very large
  - simple solutions might not scale with size in an acceptable manner
- how can we decide which option for program is most efficient?
- separate **time and space** efficiency of a program - will focus on time
- challenges in understanding efficiency of solutions to a computational problem:
  - a program can be **implemented in many different ways**
  - you can solve a problem using only a handful of diferent **algorithms**
  - would like to separate choices of implementation from choices of more abstract algorithm
- how to evaluate efficiency?
  - measured with a **timer**
  - **couting** the operations
  - abstract notion of **order of growth** (most appropriate way)
  
- Timing a program:

```python
import time

def c_to_f(c):
  return c * 9/5 + 32

t0 = time.perf_counter()
c_to_f(100000)
t1 = time.perf_counter() - t0
print('time =', t0, ':', t1, 's')
```

- But timing program is inconsistent:
  - running time **varies between algorithms**, which is what we want, *BUT*
  - it will also **vary between implementations**
  - it will also **vary between computers**
  - which makes running time **not predictable** based on small inputs to model for large data sets
  
- Counting operations

```python
def c_to_f(c):
  return c * 9/5 + 32

def mysum(x):
  total = 0
  for i in range(x+1):
    total +=1
  return total
```

- Assume these steps take **constant time**:
  - mathematical operations
  - comparisons
  - assignment
  - accessing objects in memory
- Then count the number of operations executed as function of size of input:
  - `c_to_f` has only 3 mathematical operations
  - `mysym` has one assignment, one mathematical operation on `range`, two operations (one mathematical, one assignment) on `total`, and it all loops x times.
  - so safe to say `mysum` more complex
- This method evaluates different algorithms, and changes with the algorithm, and is independent of computers
- **but** depends on implementations, and has no real definition if **which operations** to count
- Timing and counting **evaluates implementations**, but timing also **evaluates machines**, which shouldn't be a factor
- What we want is to
  - evaluate *algorithm*;
  - evaluate *scalability*;
  - evaluate in terms of *input size*
- We want to express efficiency **in terms of input**, so need to decide what your input is
  - could be an **integer*: `mysum(x)`
  - could be **length of list**: `list_sum(L)`
  - **you decide** when multiple parameters to a function: `search_for_elmt(L,e)
- Different inputs change how program runs, e.g. a function that searches for an element in a list:

```python
def search_for_elmt(L,e):
    for i in L:
        if i == e: return True
    return False
```

- **BEST CASE:** when `e` is *first element*
- **WORST CASE:** when `e` is *not in list*
- **AVERAGE CASE:** when *look through about half* of elements in list

- Suppose we are given a list `L` of some length `len(L)`
  - **best case:** minimun running time over all possible inputs of a given size, `len(L)`
    - constant for `search_for_elmt`
    - first element in any list
  - **average case:** average running time over all possible inputs of a given size `len(L)` -- a practical measure
  - **worst case:** maximum running time over all possible inputs of a given size, `len(L)`
    - linear in length of list for `search_for_elmt`
    - must search entire list and not find it
- The worst case is the most useful measure because it tells us the maximum runnning time of a function

- **ORDERS OF GROWTH** goals:
  - evaluate program's efficiency when **input is very big**
  - express the **growth of program's run time** as input size grows
  - put a **upper bound** on growth
  - do not need to be precise: **"order of" not "exact"** growth
  - we will look at the **largest factors** in run time (which section of the program will take the longest to run?)

#### 6.1.2. Big Oh Notation

- Big Oh notation measures an **upper bound on the [asymptotic growth](https://en.wikipedia.org/wiki/Asymptotic_analysis)**, often called order of growth.
- **Big Oh or O()** is used to describe worst case
  - they occur often and is the bottleneck when a program runs
  - express rate of growth of a program relative to the input size
  - evaluates algorithm, not machine or implementation
- Exact steps vs O()

```python

def fact_iter(n):
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
```

- computes factorial
- number of steps: **`1 + 5n + 1`**
- worst case aymptotic complexity:
  - **ignore** additive constants
  - **ignore** multiplicative constants
  - because of that, Big Oh notation is O(n) - **linear**

- Simplification examples:
  - drop constants and multiplicative factors
  - focus on **dominant terms**
    - `n^2 + 2n + 2` = ***O(n^2)**
    - `n^2 + 1000000n + 3^1000` = ***O(n^2)**
    - `log(n) + n + 4` = **O(n)** -- `n` is more dominant than `log(n)`
    - `0.0001 * n * lon(n) + 300n` = **O(n log n)**
    - `2n^30 + 3^n` = **O(3^n)**
- Complexity classes from Low to High:
  - **O(1)** - constant
  - **O(log n)** - logarithmic
  - **O(n)** - linear
  - **O(n log n)** - loglinear
  - **O(n^c)** - polynomial
  - **O(c^n)** - exponential

- **Analyzing programs and their complexity:**
  - **combine** complexity classes
    - analyze statements inside functions
    - apply some rules, focus on dominant term

- **Law of Addition** for O():
  - used with **sequential** statements
  - `O(f(n)) + O(g(n)) is O(f(n) + g(n))`

```python
for i in range(n):
    print('a')
for j in range (n*n):
    print('b')

# O(n) + O(n*n) = O(n + n^2) = O(n^2) because of dominant term
```

- **Law of Multiplication** for O():
  - used with **nested** statements/loops
  - `O(f(n)) * O(g(n)) is O(f(n) * g(n))`

```python
for i in range (n):
    for j in range(n):
        print('a')

# O(n) * O(n) = O(n * n) = O(n^2) because the outer loop goes n times and the inner loop goes n times for every outer loop
```

#### 6.1.3. Complexity Classes

- **O(1)** denotes constant running time
- **O(log n)** denotes logarithmic running time
- **O(n)** denotes linear running time
- **O(n log n)** denotes log-linear running time
- **O(n^c)** denotes polynomial running time
- **O(c^n)** denotes exponential running time

- **Constant complexity:**
  - complexity independent of inputs
  - can have loops or recursive calls, but number of iterations or calls independent of size of input

- **Logarithmic complexity:**
  - complexity grow as log of size of its input
  - examples:
    - bisection search
    - binary search of a list
    - *anything that divides the space of the search in half at each step is a nice example*

```python
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i / 10
    return result
```

- In this case, only have to look at loops as no function calls
- Within while loop, constant number of steps
- Have to count only how many times through loop:
  - how many times can one divide i by 10?
  - Log base 10 of the size of i: **O(log(i))**
  
- **Linear complexity:**
  - search a list in sequence to see if an element is present
  - add characters of a string, assumed to be composed of decimal digits

```python
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val
```

- All of the steps are constant (assignments and mathematical operations)
- We need only to worry how many times we go through the loop: **O(len(s))**

- but complexity can depend on number of recursive calls

```python
def fact_iter(n):
    prod = 1
    for i in range(i, n + 1):
        prod *= i
    return prod
```

- number of times around loop is `n`
- number of operations inside loop is a constant
- overall just **O(n)**
- A function that has a loop with a constant number of operations inside of it is an example of a linear complexity.
- On recursive calls:

```python
def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n - 1)
```

- if you time it, may notice that it runs a bit slower than iterative versions due to function calls
- still **O(n)** because the number of function calls is linear in n
  - recursive call is made only once for each increment
  - inside the operations are only constant operations
  - recursive function is called `n` times

- **Log-linear complexity:**
  - many practical algorithms are log-linear
  - very commonly used log-linear algorithm is merge sort

- **Polynomial Complexity:**
  - most common polynomial algorithms are quadratic, as in complexity grows with square of size of input
  - commonly occurs when we have nested loops or recursive function calls
  
```python
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
```

- The outer loop is executed len(L1) times.
- With each iteration, it will also execute the inner loop up to len(L2) times
- `**O(len(l1) * len(L2))`
- worst case when `len(L1) == len(L2)` == `n`
- **`O(n²)`**

```python
def intersect(L1, L2):
    tpm = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e1:
                tpm.append(e1)
    res = []
    for e in tpm:
        if not (e in res):
            res.append(e)
    return res
```

- First nested loop takes `len(L1) * len(L2)` steps
- Second loop takes at most `len(L1)` steps
- Latter term overwhelmed by former term
- **`O(len(L1) * len(L2))'** -> **O(n²)**

```python
def g(n):
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x
```

- computes n² very inefficiently
- when dealing with nested loops, **look at the ranges**
- nested loops, **each iterating n times**
- **O(n²)**

```python
def genSubsets(L):
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new

arr1 = [1,2,3,4]
print(genSubsets(arr1))
```

#### 6.1.4. Recursion Complexity

- Tricy complexity:

```python
def h(n):
    answer = 0
    s = str(n)
    for c in s:
        answer += int(c)
    return answer
```

- Adds digits of a number together
- linear O(len(s)) in terms of string, but what in terms of input n?
- tricky part:
  - convert integer to string
  - iterate over **length of string**, not magnitude of input n
  - think of it like dividing n by 10 each iteration
- **O(log n)** - base doesn't matter

- Complexity of Iterative Fibonacci:

```python
def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n - 1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii
```

- The loop runs linear, because only constant operations executed n times, the rest is constant.
- **`O(n)`**

```python
def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)
```

- **`O(2^n)`**

- When input is a list:

```python
def sum_list(L):
    total = 0
    for e in L:
        total += e
    return total
```

- O(n) where n is the length if the list
- O(len(L))
- must **define what size of input means**
  - previously it was the magnitude of a number
  - here, it is the length of the list
  
#### 6.1.4. Big Oh Summary

- compare **efficiency of algorithms**
  - notation that describes growth
  - **lower order of growth** is better
  - independent of machine or specific implementation
  
- use Big Oh:
  - describe order of growth
  - **asymptotic notation**
  - **upper bound**
  - **worst case** analysis

### 6.2. Searching and Sorting Algorithms

#### 6.2.1. Search Algorithms

- Search algorithm is a method for findgin an item or group of items with specific properties within a collection of items
- collection could be implicit:
  - example - finding a square root as a search problem:
    - exhaustive enumeration
    - bisection search
    - Newton-Raphson
- collection could be explicit
  - example: is a student record in a stored collection of data?
  
- Linear search:
  - brute force search
  - list does not have to be sorted
- bisection search
  - list **MUST BE SORTED** to give correct answer

- Linear search on *unsorted* list:

```python
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
```

- must go through all elements to decide it's not there
- complexity = `O(len(L)` linear
- can speed up a little by returning `True` as soon as found `e`, but doesn't impact worst case

#### 6.2.2. Bisection Search

- Doing a linear search on a **sorted list:**

```python
def search(L, e):
    for i in range(len(L)):
        if L[i]  == e:
            return True
        if L[i] > e:
            return False
    return False
```

- must only look until reach a number greater than `e`
- Overall complexity of **`O(len(L))`**

- With bisection search:
  - pick an index `i` that divides list in half
  - ask if `L[i] == e`
  - if not, ask if `L[i]` is larger or smaller than `e`
  - depending on the answer, search left or right half of `L` for `e`.
- Break into smaller version of problem (smaller list), plus some simple operations
- answer to smaller version is anwer to original problem
- Finish looking through list when `n/2^i = 1`, so `i = log n`
- Complexity is `**O(log n)**` where `n` is `len(L)`

- Bisection search implementation 1:

```python
def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)
```

- Complexity here is larger because the algorithm makes copies of the list in each call, which is demanding.

```python
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
```

- **Implementation 1:**
  - O(log n) bissection search calls
  - O(n) for each bissection call to copy list
  - **O(n log n)**
- **Implementation 2:**
  - pass list and indices as parameters
  - list never copied, just re-passed
  - **O(log n)**
- Searching a sorted list where `n == len(L)`
  - using **linear search** complexity is **O(n)**
  - using **binary search** can search for an element in **O(log n)**
    - assumes **list is sorted**
    - when does it make sens to **sort first then search**?
      - `SORT < O(n) - O(log n)`
      - when sorting is less than O(n) - **NEVER**
- So when do we sort first?
  - in some cases, may sort a list once then do many searches
  - **AMORTIZE COST** of the sort over many searches
  - `SORT + K*O(log n) < K*O(n)
  - for large `K`, **SORT time becomes irrelevant**
