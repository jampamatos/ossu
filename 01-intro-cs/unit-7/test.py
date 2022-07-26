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