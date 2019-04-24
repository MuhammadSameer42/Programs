#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#RATE OF GROWTH
import math
n = int(input("Enter Number: "))
print("log(n):",math.log(n))
print("nlog(n):",n*math.log(n))
print("n^2:",n**2)
print("n^3:",n**3)
print("n^4:",n**4)
print("n^5:",n**5)
print("n^6:",n**6)
print("n^7:",n**7)
print("n^8:",n**8)


# In[ ]:


#FINDING SERIES RESISTANCE
r = []
tr = 0
n = int(input("Enter Limit"))
for i in range(n):
    val = float(input("Enter value"))
    r.append(val)
for i in range(n):
    tr+=r[i]

print("Total Series Resistance: ",tr)


# In[ ]:


#FINDING PARALLEL RESISTANCE
r = []
tr = 0
ttr = 0
n = int(input("Enter Limit"))
for i in range(n):
    val = float(input("Enter value"))
    r.append(val)
for i in range(n):
    tr+=1/r[i]
ttr=1/tr
print("Total Parallel Resistance: ",ttr)


# In[ ]:


#ISOCELES TRIANGLE
a = float(input("Enter first side"))
b = float(input("Enter second side"))
c = float(input("Enter third side"))
if a==c or a==b or b==c:
    print("It is an isoceles triangle")
else:
    print("It is not an isoceles triangle")
    


# In[ ]:


#FINDING POWER
I = float(input("Enter Current: "))
V = float(input("Enter Voltage: "))
p = V/I
print("Power: ",p)


# In[ ]:


#FINDING CHARGE
I = float(input("Enter Current: "))
t = float(input("Enter Time: "))
q = I*t
print("Charge: ",q)


# In[ ]:


#TEMPERATURE CONVERTER
t1 = float(input("Enter temperature in Fahrenheit: "))
c = (t1-32)*5/9
print("Celcius: ",c)
t2 =float(input("Enter temperature in Celcius: "))
f = (t2 * 9/5)+32
print("Fahrenheit: ",f)


# In[ ]:


#FINAL VELOCITY
vi =int(input("Enter Initial velocity: "))
t =int(input("Enter time in seconds: "))
a =int(input("Enter Acceleration: "))
vf = vi+a*t
print("Final Velocity: ",vf)


# In[ ]:


#DISPLACEMENT
vi =int(input("Enter Initial velocity: "))
t =int(input("Enter time in seconds: "))
a =int(input("Enter Acceleration: "))
s = int((vi*t)+0.5*a*t**2)
print("Displacement: ",s)


# In[ ]:


#CONDITIONS OF TRIANGLE
a = int(input("Enter value of side one: "))
b = int(input("Enter value of side two: "))
c = int(input("Enter value of side three: "))
if a+b>c:
    print("Makes triangle")
elif a+c>b:
    print("Makes triangle")
elif c+b>a:
    print("Makes triangle")
else:
    print("Does not make triange")


# In[ ]:


#DERIVATION
from sympy import *
import numpy
eq = 5*x**3 + 6*x**2 + 4*x+ 2
x = Symbol('x')
di = eq.diff(x)
print(di)


# In[ ]:


#RESISTANCE AND CONDUCTANCE
I = int(input("Enter current: "))
V = int(input("Enter Voltage: "))
R = V/I
G = 1/R
print("Voltage: ",V)
print("Current: ",I)
print("Resistance: ",R)
print("Conductance: ",G)


# In[ ]:


#FORCE
mass = float(input("Enter Mass value: "))
acc = float(input("Enter Acceleration value: "))
force = mass*acc
S = 178
print("Mass: ",mass,"kg")
print("Accleration: ",acc,'m/s%c'%(S))
print("Force: ",force,"N")


# In[ ]:


#PYTHAGORAS THEORM
import math
per = int(input("Enter Value of Perpendicular "))
base = int(input("Enter Value of Base "))
hyp = int(input("Enter Value of Hypotenese "))
p = int(math.pow(per,2))
b = int(math.pow(base,2))
h = int(math.pow(hyp,2))
bh = b+h
print(p,"=",bh)
if p==bh:
    print("Satisfies the pythgoras theorm")
else:
    print("Does not satisfies the pythagoras theorm")


# In[ ]:


#QUADRATIC EQUATION
import cmath
d = 178
print('Enter coefficient of x%c value: '%(d))
a = int(input())
b = int(input("Enter coefficient of x value:\n"))
c = int(input("Enter constant value: "))
print('Equation = %dx%c + %dx + %d'%(a,d,b,c))
d= (b*b)-(4*a*c)
ans1 = (-b+(cmath.sqrt(d)))/2*a
ans2 = (-b-(cmath.sqrt(d)))/2*a
print("Answer 1: ",ans1)
print("Answer 2: ",ans2)


# In[ ]:


#MOMEMTUM
m = int(input("Enter value of Mass"))
vf = int(input("Enter value of final velocity"))
vi = int(input("Enter value of initial velocity"))
v = vf-vi
p = m*v
print("Momentum ",p)

