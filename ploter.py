import matplotlib.pyplot as plt
import numpy

def show(name, data):
    ''' 
        name = windown title, time = graph spacing, data = read wave file
    '''
    try:
        dat = data.astype(numpy.uint16)
        dat.setflags(write=1)
        # Time = numpy.linspace(0, len(data)/fs, num=len(data))
        plt.figure(1)
        plt.title(name)
        # plt.plot(Time, dat)
        plt.plot(data)
        plt.show()
        return True
    except:
        return False