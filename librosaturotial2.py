import numpy as np
import librosa
import IPython.display as ipd
trumpet = librosa.example("trumpet")
audio = librosa.load(trumpet)
ipd(librosa.util.example_info(trumpet))