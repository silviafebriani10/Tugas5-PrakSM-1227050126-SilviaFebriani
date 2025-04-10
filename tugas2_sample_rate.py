import librosa

# Sample rate default
y1, sr1 = librosa.load("audio1.wav")  # default 22050
print(f"Sample rate default: {sr1}, durasi: {librosa.get_duration(y=y1, sr=sr1):.2f} detik")

# Sample rate custom
y2, sr2 = librosa.load("audio1.wav", sr=16000)
print(f"Sample rate 16000: {sr2}, durasi: {librosa.get_duration(y=y2, sr=sr2):.2f} detik")

y3, sr3 = librosa.load("audio1.wav", sr=8000)
print(f"Sample rate 8000: {sr3}, durasi: {librosa.get_duration(y=y3, sr=sr3):.2f} detik")
