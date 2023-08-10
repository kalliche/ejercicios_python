'''Es uyna aplicación que se utiliza para grabar sonido y guardarlo en un formato en especifico
sudo apt update
sudo apt install portaudio19-dev

pip3 install sounddevice
pip3 install SciPy' '''

import sounddevice
from scipy.io.wavfile import write

def vioce_recoder(seconds, file):
    print('Recording Started...')
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print('Recording Finished')

vioce_recoder(10, 'record.wav')