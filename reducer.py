import wave
import numpy as np
import scipy.signal as sps
from scipy.io import wavfile
import ploter as ploter

file = "simple.wav"
fname = "reduced_" + file

class DownSample():
    def __init__(self):
        self.in_rate = 44100.0
        self.out_rate = 22050.0

    def open_file(self, file):
        try:
            self.in_wav = wave.open(file, 'r')
        except:
            print("Cannot open wav file (%s)" % str(file))
            return False

        if self.in_wav.getframerate() < self.out_rate:
            print("Error: Output rate > Input rate. File size will increase!!")
            print(self.in_wav.getframerate())
            return False

        print(self.in_wav.getframerate())
        self.in_rate = self.in_wav.getframerate()
        self.in_nframes = self.in_wav.getnframes()
        print("Frames: %d" % self.in_wav.getnframes())

        if self.in_wav.getsampwidth() == 1:
            self.nptype = np.uint8
        elif self.in_wav.getsampwidth() == 2:
            self.nptype = np.uint16
        

        return True
    
    def resample(self, fname):
        self.out_wav = wave.open(fname, "w")
        self.out_wav.setframerate(self.out_rate)
        self.out_wav.setnchannels(self.in_wav.getnchannels())
        self.out_wav.setsampwidth(self.in_wav.getsampwidth())
        # self.out_wav.setnframes(1)

        # print("Nr output chanels: %d" % self.out_wav.getnchannels())

        audio = self.in_wav.readframes(self.in_nframes)
        # audio = self.in_wav
        ploter.show('test', audio)
        nroutsamples = round((len(audio) * self.out_rate / self.in_rate))
        print("Nr output samples: %d" % nroutsamples)
        try:
            # ploter.show("Before", self.in_wav)
            self.in_wav.close()
            # audio_out = sps.resample(np.fromstring(audio, self.nptype), nroutsamples)
            audio_out = sps.resample(audio, nroutsamples)
            # audio_out = audio_out.astype(self.nptype)

            # self.out_wav.writeframes(audio_out.copy(order='C'))
            self.out_wav.writeframesraw(audio_out.copy(order='C'))

            self.out_wav.close()
            print("Saved file")
        except:
            print("Failed to resample")
            return False
        return True

def main():
    ds = DownSample()
    if not ds.open_file(file):
        return 1
    ds.resample(fname)
    return 0

if __name__ == '__main__':
    main()