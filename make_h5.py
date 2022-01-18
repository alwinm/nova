import h5py
import numpy
import os
def main():
    if os.path.isfile('trash.h5'):
        return
    
    f = h5py.File('trash.h5','w')
    
    size = 50
    
    r = (numpy.arange(size) + 0.5 - size/2)
    x = r[:,None,None]
    y = r[None,:,None]
    z = r[None,None,:]
    
    rr = r*r
    
    example = numpy.zeros([size,size,size])
    
    x0 = size/4.
    y0 = 0
    x1 = size/4. * numpy.cos(2.*numpy.pi/3)
    y1 = size/4. * numpy.sin(2.*numpy.pi/3)
    x2 = size/4. * numpy.cos(4.*numpy.pi/3)
    y2 = size/4. * numpy.sin(4.*numpy.pi/3)
    
    lim = (size/4)**2
    
    
    dist0 = (x - x0)**2 + (y - y0)**2 + z**2
    dist1 = (x - x1)**2 + (y - y1)**2 + z**2
    dist2 = (x - x2)**2 + (y - y2)**2 + z**2
    
    dist = numpy.logical_or(numpy.logical_or((dist0 <  lim),(dist1 < lim)),(dist2 < lim))

    example[dist] = 1.0
    
    phi = numpy.arctan2(r[None,:],r[:,None])
    
    radius = numpy.sqrt(rr[:,None,None] +rr[None,:,None] + rr[None,None,:])

    f.create_dataset("radius",data=radius)
    f.create_dataset("example",data=example)
    f.close()


def solution():
    with h5py.File('trash.h5','r') as _file:
        data = _file['example'][:]

    size = data.shape[0]

    print(numpy.sum(data[size//2]))
    print(numpy.sum(data[:,size//2]))
    print(numpy.sum(data[:,:,size//2]))
