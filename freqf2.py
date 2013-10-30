
from matplotlib.mlab import find
import pyaudio
import scikits.audiolab as audiolab
import numpy as np
import math
import sys
import wave

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 20


def Pitch(signal,rate):

    signal = np.fromstring(signal, 'Int16');

    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing));

    if 2*np.prod(len(signal))==0:
        return 0
    else:
        f0= round(len(index) * rate /(2*np.prod(len(signal))))
        return f0;

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)
wf = wave.open(sys.argv[1], 'rb')
p = pyaudio.PyAudio()
#stream = p.open(format = FORMAT,
#channels = CHANNELS,
#rate = RATE,
#input = True,

#output = True,
#frames_per_buffer = chunk)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
data=wf.readframes(chunk)
#for i in range(0, wf.getframerate() / chunk * RECORD_SECONDS):
 #   data = stream.read(chunk)
  #  Frequency=Pitch(data)
   # print "%f Frequency" %Frequency
while data != '':
    stream.write(data)
    data = wf.readframes(chunk)
    Frequency=Pitch(data,wf.getframerate())
    print str(Frequency)+" Frequency"

stream.stop_stream()
stream.close()

p.terminate()