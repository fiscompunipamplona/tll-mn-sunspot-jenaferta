from pylab import plot, show
x=[]
y=[]
for i in range(10):
    y.append(i*i)
    x.append(2*i)
#plot (x,y)
show()


from numpy import linspace, sin

x=linspace (0, 10, 100)
y=sin(x)
#plot(x,y)
show()

a=open("test.dat", "w")
for i in range(len(x)):
    a.write("%.2f %.2f\n" % (x[i],y[i]))
a.close()
from numpy import loadtxt

b=loadtxt("test.dat", float)
print(b[:,0])
print(b[:,1])

plot(b[:,0],b[:,1])
show()
from numpy import linspace, cos

z=linspace(0, 10, 100)
x=sin(z)
y=cos(z)

plot (z,x,"r--")
plot (z,y,"yo")
show()
