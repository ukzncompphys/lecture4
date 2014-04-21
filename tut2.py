#The correlation function f (star) g is integral of f(x)g(x+y).  Through a similar
#proof, one can show f(star) g=ift(dft(f)*conj(dft(g))).  Write a routine to
#take the correlation function of two arrays.  Plot the correlation
#function of a Gaussian with itself.  

from numpy.fft import fft,ifft
import numpy
from matplotlib import pyplot as plt

def mycorr(x,y):
    assert(x.size==y.size)  #if the vectors are different sizes, get grumpy
    xft=fft(x)
    yft=fft(y)
    yftconj=numpy.conj(yft)
    return numpy.real(ifft(xft*yftconj))

if __name__=='__main__':
        x=numpy.arange(-20,20,0.1)
        sigma=2
        y=numpy.exp(-0.5*x**2/sigma**2)
        
        ycorr=mycorr(y,y)
        plt.plot(x,ycorr)
        plt.show()
        



