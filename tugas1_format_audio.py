import librosa

# Format WAV
y_wav, sr_wav = librosa.load("audio1.wav", sr=None)
print(f"WAV - Sample Rate: {sr_wav}, Durasi: {librosa.get_duration(y=y_wav, sr=sr_wav):.2f} detik")

# Format MP3
y_mp3, sr_mp3 = librosa.load("audio_example.mp3", sr=None)
print(f"MP3 - Sample Rate: {sr_mp3}, Durasi: {librosa.get_duration(y=y_mp3, sr=sr_mp3):.2f} detik")
