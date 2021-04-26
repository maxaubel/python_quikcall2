import pyaudio
import numpy as np

CHUNK = 2**11 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device

'''# create a numpy array holding a single read of audio data
for i in range(10): #to it a few times just to see
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    print(max(data))
'''

for i in range(int(10*44100/1024)): # a few seconds
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    peak = np.average(np.abs(data))*2
    bars = "#"*int(50*peak/2**12)
    print("%04d %05d %s"%(i,peak,bars))

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()
