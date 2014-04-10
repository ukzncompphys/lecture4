from numpy import arange,exp,real,conj
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt
def conv(f,g):
    ft1=fft(f)
    ft2=fft(g)
    return real(ifft(ft1*ft2))
    
def corr(f,g):
    ft1=fft(f)
    ft2=fft(g)
    return real(ifft(ft1*conj(ft2)))

def shift(f,n):
    g=0*f
    g[n]=1
    return ifft(fft(f)*fft(g))

def mycorr(f,n):
    ff=shift(f,n)
    return corr(ff,ff)

x=arange(-10,20,0.1)
f=exp(-0.5*(x+3)**2/0.5**2)

g1=mycorr(f,0)
g2=mycorr(f,10)
g3=mycorr(f,50)
plt.plot(g1,'r')
plt.plot(g2,'k')
plt.plot(g3,'b')
plt.show()
