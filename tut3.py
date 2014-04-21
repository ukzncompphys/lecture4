#Using the results of part 1 and part 2, write a routine to take the
#correlation function of a Gausian (shifted by an arbitrary amount)
#with itself.  How does the correlation function depend on the shift?
#Does this surprise you? 

from numpy.fft import fft,ifft
import numpy
from matplotlib import pyplot as plt
def myshift(x,n=0):
    '''myshift(x,n): shift an array x by an amount n using FFTs'''
    vec=0*x  #make a vector of zeros the same length as the input vector
    vec[n]=1
    vecft=fft(vec)
    xft=fft(x)
    return numpy.real(ifft(xft*vecft))



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
        yshift=myshift(y,y.size/4)
        yshiftcorr=mycorr(yshift,yshift)
        meanerr=numpy.mean(numpy.abs(ycorr-yshiftcorr))
        print 'mean difference between the two correlation functions is ' + repr(meanerr)
        plt.plot(x,ycorr)
        plt.plot(x,yshiftcorr)        
        plt.show()
        

