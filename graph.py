import matplotlib.pyplot as plt

from matplotlib import style

plt.title('graph')
x = [2,5,3]
y = [4,6,2]
plt.plot(x,y,'b',label="example",linewidth=3)
plt.legend()
plt.xlabel('time')
plt.ylabel('frequency')
plt.grid(True,color= 'r')