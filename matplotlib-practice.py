"""
    PRACTICE OF matplotlib MODULE
"""

import numpy as np
import matplotlib.pyplot as pyplot
import random

def basic_graph():
    x = np.arange(1, 21, 1.5)
    y1 = np.log(x)
    y2 = np.cos(x)
    y3 = np.sin(x)

    pyplot.plot(x, y1, marker = "d", linestyle = "solid", label="log(x)")
    pyplot.plot(x, y2, marker = "*", linestyle = "dotted", label="cos(x)")
    pyplot.plot(x, y3, marker = "p", linestyle = "dashdot", label="sin(x)")
    pyplot.legend(loc = "best")
    pyplot.xticks(x)
    pyplot.xlabel("x")

    #pyplot.savefig("C:\\Users\\user-10\\Desktop\\Class XII\\lmfao.pdf")
    pyplot.show()

def barchart():

    classes = ['IX', 'X', 'XI', 'XII']
    students = [68, 72, 46, 34]
    marks = [46,57,51,68]
    xticks = np.arange(4)

    pyplot.bar(xticks - 0.15, students, width = 0.3, label = "Students", color = "blue")
    pyplot.bar(xticks + 0.15, marks, width = 0.3, label = "Avg marks", color = "red")
    pyplot.title("high skool dumb kiddos")
    pyplot.xlabel("Classes")
    pyplot.ylabel("Value")
    pyplot.legend(loc = "best")
    pyplot.xticks(xticks, classes)
    pyplot.yticks(np.arange(0, 101, 10))
    pyplot.show()

''' PRACTICE QUESTION: rainfall in mm, zones - 5 zones, months jan to july
    north: 140, 130, 130, 190, 160, 200, 150
    east: 140, 180, 150, 170, 190, 140, 170
    south: 160, 200, 130, 200, 200, 170, 110
    west: 180, 150, 200, 120, 180, 140, 110
    central: 110, 160, 130, 110, 120, 170, 130
'''
def weather_chart():
    zones = ['north', 'east', 'south', 'west', 'central']
    north = [140, 130, 130, 190, 160, 200, 150]
    east = [140, 180, 150, 170, 190, 140, 170]
    south = [160, 200, 130, 200, 200, 170, 110]
    west = [180, 150, 200, 120, 180, 140, 110]
    central = [110, 160, 130, 110, 120, 170, 130]

    markers = ['*', 'o', 'd', 'p', 's']
    linestyles = ['solid', 'dashed', 'dashdot']
    ticks = np.arange(100, 210, 10)

    for zone in zones:
        pyplot.plot(ticks, eval(zone), marker = ramdom.choice(markers), linestyle = random.choice(linestyles), label = "%s zone" % zone)
    
