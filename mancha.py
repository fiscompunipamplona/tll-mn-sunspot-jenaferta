from numpy import loadtxt
from pylab import plot, show, xlim

a=loadtxt("sunspots.txt", float)

plot(a[:,0],a[:,1])
show()

plot (a[:,0],a[:,1])
xlim(0,1001)
show()

from numpy import zeros
r=5
y=zeros(1000,float)

#for k in range (0,1001):
   # for m in range (-r,r):
       # y(k)=(1/(2r+1))
