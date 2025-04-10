import librosa
import librosa.display
import matplotlib.pyplot as plt

file_audio = 'audio_example.wav'
y, sr = librosa.load(file_audio, sr=None)

plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform Audio")
plt.xlabel("Waktu (detik)")
plt.ylabel("Amplitudo")
plt.tight_layout()
plt.show()