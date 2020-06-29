# import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def plotWave(filename):
    print('test')
    # rate, data = wav.read(filename)
    fs, data = wavfile.read(filename)
    print(fs)
    left = np.array([])
    right = np.array([])
    # print(left)

    # this is very slow to 
    # for item in data:
    #     # store left values
    #     temp = np.array([item[0]])
    #     left = np.append(left, temp)
    #     # store right values
    #     temp = np.array([item[1]])
    #     right = np.append(right, temp)
    
    # print(left[0])
    # print(right[0])
    N, __ = data.shape 
    print(N)
    total_time = float(N/fs)
    print(total_time)

    # interval
    time = np.linspace(0,total_time,N)
    plt.plot(time, data[:,0])
    # plt.plot(time, data[:,1])
    plt.show()
    

    

def main():
    path = './sounds/Alesis-Fusion-Acoustic-Bass-C2.wav'
    plotWave(path)

if __name__ == '__main__':
    main()