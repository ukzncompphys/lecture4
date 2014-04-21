#Write a function that will shift an array by an arbitrary amount
#using a convolution (yes, I know there are easier ways to do this).
#The function should take 2 arguments - an array, and an amount by
#which to shift the array.  Plot a gaussian that started in the centre
#of the array shifted by half the array length 

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

if __name__=='__main__':
    x=numpy.arange(-20,20,0.1)
    sigma=2
    y=numpy.exp(-0.5*x**2/sigma**2)
    yshift=myshift(y,y.size/2)
    
    plt.ion()
    plt.plot(x,y)
    plt.plot(x,yshift)

