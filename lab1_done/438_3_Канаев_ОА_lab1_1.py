import numpy as np                 #Used for arrays
import matplotlib.pyplot as plt    #Used for graphics
from math import *                 #Used for math_functions
import time                        #Used for time_management

ELEMS = 10000
left_border = 0
right_border = 10

x = np.linspace(left_border, right_border, ELEMS)  #Evenly spaced X axis (endpoint = False)
y = np.sin(x)  #Function

def x_axis(x_):
    x_rol = np.zeros(ELEMS)
    x_rol[0:ELEMS - 1] = x_[1:ELEMS]
    x_rol[-1] = x_[-1]
    x_dif = x_rol - x_
    return x_dif


def rect_with_numpy(y_, x_dif):
    integral_rectangle = (y_ * x_dif).sum()
    return integral_rectangle


def trap_with_numpy(y_, x_dif):
    y_rol = np.zeros(ELEMS)
    y_rol[0:ELEMS - 1] = y_[1:ELEMS]
    y_rol[-1] = y_rol[-2]
    y_sum = ((y_ + y_rol) * 0.5 * x_dif).sum()
    integral_trapeze = y_sum
    return integral_trapeze



start_time = time.time()   #save current time
for i in range(99):
    rect_with_numpy(y, x_axis(x))
print(f"\nintegral by rectangle with numpy = {rect_with_numpy(y, x_axis(x))}")
print("--> %s seconds <--\n" % (time.time() - start_time))  #Output execution time


start_time = time.time()   #save current time
for i in range(99):
    trap_with_numpy(y, x_axis(x))
print(f"integral by trapeze with numpy = {trap_with_numpy(y, x_axis(x))}")
print("--> %s seconds <--" % (time.time() - start_time))  #Output execution time

########################################without_numpy############################################
x1 = [i for i in range(ELEMS)] #Init array
x2 = [(right_border-left_border)*i/(ELEMS-1) for i in range(ELEMS)] #(ELEMS-1) because this's number of pieces
y1 = [sin(x2[i]) for i in range(ELEMS)]

ax1 = plt.gca()
plt.plot(x2, y1)
plt.plot(x+0.1, y+0.1)
plt.title("WithOut Numpy")
ax1.set_xlabel("angel, rad")
ax1.set_ylabel("sin(x)")
plt.show()


def x_axis_2(x2_):
    x_dif1 = []
    x_dif1[0:ELEMS - 1] = x2_[1:ELEMS]
    x_dif1.append(x2[ELEMS - 1])
    x_dif1 = [x_dif1[i] - x2_[i] for i in range(ELEMS)]
    return x_dif1


def rect_without_numpy(y1_, x_dif1):
    integral_rectangle1 = 0.0
    for i in range(ELEMS):

        integral_rectangle1 += y1_[i] * x_dif1[i]
    return integral_rectangle1


def trap_without_numpy(y1_, x_dif1):
    integral_trapeze1 = 0
    for i in range(ELEMS-1):
        integral_trapeze1 += ((y1_[i] + y1_[i+1]) * 0.5 * x_dif1[i])
    return integral_trapeze1


start_time = time.time()   #save current time
for i in range(99):
    rect_without_numpy(y1, x_axis_2(x2))
print(f"\n\nintegral by rectangle without numpy = {rect_without_numpy(y1, x_axis_2(x2))}")
print("--> %s seconds <--" % (time.time() - start_time))  #Output execution time

start_time = time.time()   #save current time
for i in range(99):
    trap_without_numpy(y1, x_axis_2(x2))
print(f"integral by trapeze without numpy = {trap_without_numpy(y1, x_axis_2(x2))}")
print("--> %s seconds <--" % (time.time() - start_time))  #Output execution time

ax1 = plt.gca()
plt.plot(x2, y1)
plt.plot(x+0.1, y+0.1)
plt.title("WithOut Numpy")
ax1.set_xlabel("angel, rad")
ax1.set_ylabel("sin(x)")
plt.show()


print(f"\n\n{np.array(x_axis_2(x2))-x_axis(x)}")
print(f"\n{np.array(y1)-y}")

print(f"\n\n{y*x_axis(x)  -  np.array(y1)*np.array(x_axis_2(x2))}\n\n")

