"""
  Physics Class assignment
  Author: Eric Shih
  Date: 2019/4/19
"""

from vpython import *

# physical const setting
k = 9*10**9 # k for n2 
em = 9.10938356 * 10**(-31) # electron's mass
r = 25

# others constent
c1 = 3*10**(-9) # right point +3.00nC
c2 = 2*10**(-9) # left point +2.00nC
e = (-1.602) * 10 ** (-19) # electron charge
t = 0  # total time
dt = 0.00000001  # small time 

bSize = 1 # point size

# electron's acceleration
ea = ( ((k*c1*e)/r**2) - ((k*c2*e)/((0.5-r)**2)) ) / em 
print("ea: ", ea)


# main code
scene = canvas(title="Exercise Simulation" , width = 600, height = 600, x = 0, y = 0, center = vector(0, 0, 0), background = vector(0, 0.6, 0.6))
pe = sphere(pos = vector(0, 0, 0), radius = bSize, color = color.blue)
pe.v = vector(0, 0, 0)
pe.a = vector(ea, 0, 0)
p1 = sphere(pos = vector(-25, 0, 0), radius = bSize, color = color.red)
p2 = sphere(pos = vector(25, 0, 0), radius = bSize, color = color.red)

gd = graph(title = "F/t", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", ytitle = "a(cm/s^2)")
eat = gcurve(graph = gd, color = color.blue) 



print("first ea: ", ea)
while( (pe.pos.x - p1.pos.x) >= 10 ):
  rate(1000)
  pe.a = vector(ea, 0, 0)
  # print("pe.a: ", pe.a)
  pe.v += pe.a * dt
  pe.pos += pe.v * dt
  r = r + (pe.v.x * dt)
  ea = ( ((k*c1*e)/r**2) - ((k*c2*e)/((0.5-r)**2)) ) / em
  eat.plot(pos = (t,(-ea)))
  t += dt


# test Data
print("last ea: ", ea)
print("r", r)
print("p1: ", p1.pos)
print("p2: ", p2.pos)
print("pe: ", pe.pos)
print("t = ", t)
  

