import numpy
import pylab

def a():
    x = numpy.arange(1000) # integers from 0 to 1000
    
    # divide by 1000 so that x goes from 0 to 1
    # multiply by 2 pi so that x covers a full oscillation
    angle = (2*numpy.pi/1000)*x
    pylab.plot(angle,numpy.sin(angle))


def b():
    # linspace starting at 0 and ending at 2*pi, with 1000 points
    x = numpy.linspace(0,2*numpy.pi,1000)
    pylab.plot(x,numpy.sin(x))

def c():
    # arange from 0 to 2*pi, but with step size 2*numpy.pi/1000 so that there are 1000 points
    x = numpy.arange(0,2*numpy.pi,2*numpy.pi/1000.)
    pylab.plot(x,numpy.sin(x))

def d():
    # plot two oscillations and plot x in degrees
    x = numpy.arange(1000)
    angle = (4*numpy.pi/1000)*x
    degrees = 180*angle/numpy.pi
    pylab.plot(degrees,numpy.sin(angle))
