"""
    PRACTICE OF matplotlib MODULE
"""

import numpy as np
import matplotlib.pyplot as pyplot

x = np.arange(1, 21, 1.5)
y1 = np.log(x)
y2 = np.cos(x)
y3 = np.sin(x)

pyplot.plot(x, y1, marker = "d", linestyle = "solid", label="log(x)")
pyplot.plot(x, y2, marker = "*", linestyle = "dotted", label="cos(x)")
pyplot.plot(x, y3, marker = "p", linestyle = "dashdot", label="sin(x)")
pyplot.legend(loc="upper left")
pyplot.xticks(x)
pyplot.xlabel("x")

#pyplot.savefig("C:\\Users\\user-10\\Desktop\\Class XII\\lmfao.pdf")
pyplot.show()
