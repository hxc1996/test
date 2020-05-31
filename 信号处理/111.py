import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
sampling_freq1, audio1 = wavfile.read('audio\FS.wav')
print(sampling_freq1)
audio1=audio1[:,0]
N=len(audio1)
t=np.arange(N)/sampling_freq1
fit=plt.figure(figsize=(8,6))
ax=plt.subplot(221)
ax.set_title('女S时域')
plt.xlabel('time(s)')
plt.plot(t,audio1)

audio1=fftshift(fft(audio1))
f=-sampling_freq1/2+np.arange(0,N,1.0)*sampling_freq1/(N-1)
ax2=plt.subplot(222)
ax2.set_title('女S频域')
plt.xlim([0,10000])
plt.xticks()
plt.xlabel('Hz')
plt.plot(f,abs(audio1))


sampling_freq2, audio2 = wavfile.read('audio\MS.wav')
print(sampling_freq2)
audio2=audio2[:,0]
N=len(audio2)
t=np.arange(N)/sampling_freq2
ax1=plt.subplot(223)
ax1.set_title('男S时域')
plt.xlabel('time(s)')
plt.plot(t,audio2)


audio2=fftshift(fft(audio2))
f=-sampling_freq2/2+np.arange(0,N,1.00)*sampling_freq2/(N-1)
ax2=plt.subplot(224)
ax2.set_title('男S频域')
plt.xlim([0,10000])
plt.xticks()
plt.xlabel('Hz')
plt.plot(f,abs(audio2))

plt.tight_layout()
plt.show()
