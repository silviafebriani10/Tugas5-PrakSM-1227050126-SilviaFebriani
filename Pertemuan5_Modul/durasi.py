import librosa
import scipy.io.wavfile

file_audio = 'audio_example.wav'

# Librosa
y, sr = librosa.load(file_audio, sr=None)
duration_librosa = librosa.get_duration(y=y, sr=sr)
print(f"Durasi (Librosa): {duration_librosa:.2f} detik")

# Scipy
sr_scipy, y_scipy = scipy.io.wavfile.read(file_audio)
duration_scipy = len(y_scipy) / sr_scipy
print(f"Durasi (Scipy): {duration_scipy:.2f} detik")