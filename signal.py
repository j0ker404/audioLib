import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

class AudioSignal:

    def __init__(self, filename):
        fs, data = wavfile.read(filename)
        self._fs = fs
        self._data = data