import librosa
import librosa.display
import matplotlib.pyplot as plt

def tampilkan_waveform(judul, file):
    y, sr = librosa.load(file, sr=None)
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title(judul)
    plt.xlabel("Waktu (detik)")
    plt.ylabel("Amplitudo")
    plt.tight_layout()
    plt.show()

tampilkan_waveform("Waveform Musik", "musik.wav")
tampilkan_waveform("Waveform Suara Manusia", "manusia.wav")
tampilkan_waveform("Waveform Suara Lingkungan", "lingkungan.wav")
