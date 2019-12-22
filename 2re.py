from scipy.io import wavfile
import os.path
from os import path
from pydub import AudioSegment
import scipy.signal as sps
import numpy as np
import matplotlib.pyplot as plt
import librosa
import sys

args = sys.argv
args = args[1:]

# Your new sampling rate
new_rate = 3200
if(len(args) == 0):
    print("Please enter filename")
    quit()
if(not path.exists(args[0])):
    print("File not found")
    quit()
if(len(args) == 1):
    print("Downsampling to default: {}".format(new_rate))
if(len(args) == 2):
    try:
        float(args[1])
        new_rate = int(args[1])
    except Exception as err:
        print(err)



filename = args[0]
src = filename

data = 0
sampling_rate = 0
fileType = src[-4:]
# Read file
if(fileType == '.wav'):
    sampling_rate, data = wavfile.read(src)
    print(data)
    print(type(data))
    print(sampling_rate)
    plt.figure(figsize=(12,4))
    plt.plot(data)
    plt.show()
elif(fileType == '.mp3'):
    data, sampling_rate = librosa.load(path=src)
    # print(data)
    # print(type(data))
    # print(sampling_rate)
    toWav = AudioSegment.from_mp3(src)
    data = toWav.get_array_of_samples()
    data = np.array(data)
    if toWav.channels == 2: data = data.reshape((-1, 2))
    sampling_rate = toWav.frame_rate
    
    print(data)
    print(type(data))
    print(sampling_rate)
    plt.figure(figsize=(12,4))
    plt.plot(data)
    plt.show()
else:
    print("Support only mp3 and wav formats")
    quit()

# print("Original :\n{}".format(data))
# Resample data
number_of_samples = round(len(data) * float(new_rate) / sampling_rate)

print(number_of_samples)
print(type(data))
print(data.shape)
try:
    data = sps.resample(data, number_of_samples)
    data = np.asarray(data, dtype=np.int16)
    # print("Processed :\n{}".format(data))
except:
    print("Error: Can't process file!")
    quit()

try:
    # data = np.asarray(data, dtype=np.float)
    # librosa.output.write_wav("./output/mini_{}.wav".format(src[:-4]), data, new_rate)

    wavfile.write("output/mini_{}".format(src), new_rate, data)
    print("File saved to output/mini_{}.wav with Sampling at {}".format(src, new_rate))
except:
    print("Error: Can't write file!")
