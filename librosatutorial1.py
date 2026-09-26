# %%

import librosa
from IPython.display import HTML, display
import matplotlib.pyplot as plt
import numpy

filename = librosa.example("trumpet")
y , sr = librosa.load(filename)   # y is the audio signal, sr is the sampling rate .
### default sampling rate is 22050 (22050 samples per second)

time = y.__len__()/sr
print(time)
# or 
print(librosa.get_duration(y=y, sr=sr))
# Listening to audio
from IPython.display import Audio , display
display(Audio(data=y, rate=sr))


# plot the audio signal
plt.figure(figsize=(12, 4))
plt.plot(y)
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.title("Audio Signal")
plt.show()


# %%
