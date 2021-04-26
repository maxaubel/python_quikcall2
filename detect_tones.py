import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import time 
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed


np.set_printoptions(suppress=True)

def send_to_discord(message):
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/836305348863197194/caX7oB-etv7XnfKAVL0ByD-irCD7LRC4L_ekuN0JLUftzLTHka20loiCxyLXGgTHxEcD', 
    username="Central CBVM",
    content = message)

    response = webhook.execute()
    

def get_code(freq, codes, threshold):
    dist = {}

    for i in codes:
        dist[i] = abs(i - freq)

    if min(dist.values()) > threshold:
        return 0
    else:
        return codes[ min(dist, key=dist.get) ]

CHUNK = 4096 # 8192 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)
DIV = 32

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True, frames_per_buffer=CHUNK)

quik_call_freqs = {553.9: 150, 584.8: 151, 617.4: 152, 651.9: 153, 688.3: 154, 726.8: 155,
                   767.4: 156, 810.2: 157, 855.5: 158, 903.2: 159, 953.7: 160}

companias = {151: 1, 152: 2, 153: 3, 154: 4, 155: 5,
             156: 6, 157: 7, 158: 8, 159: 9, 160: 10}

tones_counter = 0
tones_open = 0
last_code = 0

listening = False
listening_open = 0

while(1):
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    data = data * np.hanning(len(data))

    fft = abs(np.fft.fft(data).real)
    fft = fft[:int(len(fft)/DIV)]
    
    freq = np.fft.fftfreq(CHUNK,1.0/RATE)
    freq = freq[:int(len(freq)/DIV)]

    freqPeak = freq[np.where(fft==np.max(fft))[0][0]]+1

    code = get_code(freqPeak, quik_call_freqs, 10)

    if (code == 150) and (not listening):
        listening = True
        listening_open = time.time()
        
    if time.time() - listening_open >= 1.5:
        listening = False
        tones_counter = 0

    if listening and code != 150 and code != 0:
        if tones_counter == 0:
            tones_open = time.time()
            last_code = code
        
        if code == last_code:
            tones_counter += 1

    if tones_counter > 4 and time.time()-tones_open<2 and code==last_code:
        print("\n\n!!!!!!!!!!!!")
        print(f"tono {companias[code]} compañía a las {datetime.now()}")
        send_to_discord(f"tono {companias[code]} compañía a las {datetime.now()}")

        listening = False
        tones_counter = 0
            
        #print(f"{freqPeak} Hz, code: {code}")
        #print(f"tono {companias[code]} compañía")


stream.stop_stream()
stream.close()
p.terminate()