import matplotlib.pyplot as plt
l1=[30,18,10,23]
l2=['VII','IX','X','XI']
clr=['blue','red','green','yellow']
ex=[0.2,0,0,0.2]
plt.pie(l1)
plt.pie(l1,labels=l2,colors=clr,autopct='%3d%%',explode=ex)
plt.show()
