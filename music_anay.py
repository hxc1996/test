import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift, ifft

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
sampling_freq1, audio1 = wavfile.read('audio\FM.wav')
print(sampling_freq1)
audio1=audio1[:,0]
N=len(audio1)
t=np.arange(0,N,1.000)/sampling_freq1
fit=plt.figure(figsize=(8,6))
ax=plt.subplot(121)
ax.set_title('女生时域')
plt.xlabel('time(s)')
plt.plot(t,audio1)

audio1=fftshift(fft(audio1))
f=-sampling_freq1/2+np.arange(0,N,1.0)*sampling_freq1/(N-1)
ax2=plt.subplot(122)
ax2.set_title('女生频域')
plt.xlabel('Hz')
plt.xlim([0,22050])
plt.plot(f,abs(audio1))

plt.tight_layout()
plt.show()
