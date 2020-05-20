import librosa
y,sr = librosa.load("M.wav")
b = librosa.effects.pitch_shift(y, sr, n_steps=10)
librosa.output.write_wav("M5.wav",b,sr)
