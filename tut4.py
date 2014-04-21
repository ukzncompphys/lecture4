#The circulant (wrap-around) nature of the dft can sometimes be
#problematic.  Write a routine to take the convolution of two arrays
#*without* any danger of wrapping around.   You may wish to add zeros
#to the end of the input arrays.  


from numpy.fft import fft,ifft
import numpy
from matplotlib import pyplot as plt

def conv_nowrap(x,y):
    assert(x.size==y.size)  #if the vectors are different sizes, get grumpy
    #now we need to make double length arrays padded with zeros at the end
    #this way a value at the end of the first array convolved with a value at
    #the end of the second array will end up at the end of the padded array
    xx=numpy.zeros(2*x.size)
    xx[0:x.size]=x

    yy=numpy.zeros(2*y.size)
    yy[0:y.size]=y
    xxft=fft(xx)
    yyft=fft(yy)
    vec=numpy.real(ifft(xxft*yyft))
    return vec[0:x.size]

if __name__=='__main__':
    x=numpy.arange(-20,20,0.1)
    sigma=2
    y=numpy.exp(-0.5*x**2/sigma**2)
    y=y/y.sum()

    yconv=conv_nowrap(y,y)
    plt.plot(x,y)
    plt.plot(x,yconv)
    plt.show()

    
