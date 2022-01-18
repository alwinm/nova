import numpy
import pylab
import h5py
import os

def main():
    if not os.path.isfile('trash.h5'):
        print('Generate trash.h5 first!')
        return
    with h5py.File('trash.h5','r') as _file:
        data = _file['example'][:]

    size = len(data)
        
    pylab.subplot(2,3,1)
    pylab.pcolormesh(data[size//2])
    pylab.title('X slice')
    
    pylab.subplot(2,3,2)
    pylab.pcolormesh(data[:,size//2])
    pylab.title('Y slice')
    
    pylab.subplot(2,3,3)
    pylab.pcolormesh(data[:,:,size//2])
    pylab.title('Z slice')
    
    pylab.subplot(2,3,4)
    pylab.pcolormesh(data.sum(axis=0))
    pylab.title('X projection')
    
    pylab.subplot(2,3,5)
    pylab.pcolormesh(data.sum(axis=1))
    pylab.title('Y projection')
    
    pylab.subplot(2,3,6)
    pylab.pcolormesh(data.sum(axis=2))
    pylab.title('Z projection')

    pylab.tight_layout()


def histogram():
    with h5py.File('trash.h5','r') as _file:
        data = _file['radius'][:]

    pylab.hist(data.flatten(),bins=30)


def correlation():
    with h5py.File('trash.h5','r') as _file:
        x = _file['example'][:].flatten()
        r = _file['radius'][:].flatten()

    
    pylab.subplot(1,2,1)
    pylab.scatter(x,r,marker='.',s=1,alpha=0.3)
    
    pylab.subplot(1,2,2)
    pylab.hist2d(x,r)
    
