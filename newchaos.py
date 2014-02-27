import numpy as np
import matplotlib.pyplot as plt


r=1+np.sqrt(8)
r=3.5
x0 = 0.3
n= 100
x=[]
y=[]
j=0
x.append(r*x0*(1-x0))
y.append(j)
for i in range(0,n+1):
    i=r*x[i]*(1-x[i])
    x.append(i)

    j+=1
    y.append(j)

plt.plot(y,x)
plt.show()

yf = np.abs(np.fft.fft(x))**2
yf = np.fft.fft(x)
dataF = np.abs(np.fft.fftshift(np.fft.fft(x)))
#dataF = np.abs((np.fft.fft(x)))

#plt.plot(yf,x)
#plt.plot(y,yf)
plt.plot(dataF)
plt.show()



#Liapunov Exponent
lyap = np.zeros((1000))
j=0;
#for(r=3:0.001:4)
#rs = np.arange(3,4,0.001)
r = np.arange(3,4,0.001)
#for r in rs:
xn1=np.random.rand(1);
lyp=0;
for k in xrange(0,10000):
    xn=xn1;
    #logistic map
    xn1=r*xn*(1-xn);
    #wait for transient
    if k>300:
        # calculate the sum of logarithm
        lyp=lyp+np.log(abs(r-2*r*xn1));
    #end
#end
#%calculate lyapun
lyp=lyp/10000;

#print lyp
lyap=lyp;
j=j+1;
#end
#r=3:0.001:4;
r = np.arange(3,4,0.001)
plt.plot(r,lyap);
plt.show()
