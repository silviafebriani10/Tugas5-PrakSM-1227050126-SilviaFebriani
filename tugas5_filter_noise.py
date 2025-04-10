import librosa
import scipy.signal
import matplotlib.pyplot as plt

file = "lingkungan.wav"
y, sr = librosa.load(file, sr=None)

# Filter low-pass untuk menghilangkan noise frekuensi tinggi
sinyal_filtered = scipy.signal.lfilter([1.0], [1.0, -0.95], y)

plt.figure(figsize=(10, 6))

# Sebelum filter
plt.subplot(2, 1, 1)
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform Asli (Dengan Noise)")

# Setelah filter
plt.subplot(2, 1, 2)
librosa.display.waveshow(sinyal_filtered, sr=sr)
plt.title("Waveform Setelah Filter (Noise Berkurang)")

plt.tight_layout()
plt.show()
