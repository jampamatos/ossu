# INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES

## TABLE OF CONTENTS

- [INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING USING PYTHON -- NOTES](#introduction-to-computer-science-and-programming-using-python----notes)
  - [TABLE OF CONTENTS](#table-of-contents)
  - [UNIT 7 - PLOTTING](#unit-7---plotting)
    - [7.1. Plotting](#71-plotting)
      - [7.1.1. Visualizing Results](#711-visualizing-results)
      - [7.1.2. Using Pylab](#712-using-pylab)
      - [7.1.3. Simple Example](#713-simple-example)

## UNIT 7 - PLOTTING

### 7.1. Plotting

#### 7.1.1. Visualizing Results

- earlier saw examples of different orders of growth of procedures
- used graphs to provide an intuitive sense of differences
- example of leveraging an existing librarym rather than writing procedures from scratch
- Python provides libraries for (among others);
  - graphing
  - numeral computation
  - stochasti computation
- want to explore idea of using existing library procedures to guide processing and exploration of data

#### 7.1.2. Using Pylab

- can import library into computing environment

```python
import matplotlib.pyplot as plt
```

- allows me to reference any lybrary procedure as `plt.<procName>`
- provides access to existing set of graphing/plotting procedures
- here will just show some simple examples, lots of additional information available in documentation associated with `pylab`

#### 7.1.3. Simple Example

- basic function plots two lists as `x` and `y` values
- first, let's generate some example data

```python
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
  mySamples.append(i)
  myLinear.append(i)
  myQuadratic.append(i**2)
  myCubic.append(i**3)
  myExponential.append(1.5**i)
```

- to generate a plot, call

```python
plt.plot(mySamples, myLinear)
```

- arguments are list of values (lists must be of same length)
- calling function in a iPython console will generate plots within that console
- calling function in a Python console will create a separate window in which plot is displayed.

```python
import matplotlib.pyplot as plt

from cProfile import label
import matplotlib.pyplot as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
  mySamples.append(i)
  myLinear.append(i)
  myQuadratic.append(i**2)
  myCubic.append(i**3)
  myExponential.append(1.5**i)

plt.figure('lin')
plt.clf()   # clear previous plot
plt.title('Linear')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear, 'b-', linewidth = 4.0)  # blue line

plt.figure('quad')
plt.clf()
plt.title('Quaratic')
plt.xlabel('sample points')
plt.ylabel('quadratic function')
plt.plot(mySamples, myQuadratic, 'ro')               # red circles

plt.figure('cube')
plt.clf()
plt.title('Cubic')
plt.xlabel('sample points')
plt.ylabel('cubic function')
plt.plot(mySamples, myCubic, 'g^')                   # triangle green

plt.figure('expo')
plt.clf()
plt.title('Exponential')
plt.xlabel('sample points')
plt.ylabel('exponential function')
plt.plot(mySamples, myExponential, 'r--')            # dotted red

plt.figure('lin quad')
plt.clf()
plt.title('Linear vs. Quadratic')
plt.plot(mySamples, myLinear, label = 'linear')
plt.plot(mySamples, myQuadratic, label = 'quadratic')
plt.legend(loc = 'upper left')

plt.figure('cube expo')
plt.clf()
plt.title('Cubic vs Exponential')
plt.plot(mySamples,myCubic, label= 'cubic')
plt.plot(mySamples, myExponential, label = 'exponential')
plt.legend()


plt.show()
```
