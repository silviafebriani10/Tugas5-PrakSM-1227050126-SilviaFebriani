# Modul Praktikum 5 - Sistem Multimedia
## Teknik Informatika, UIN Sunan Gunung Djati Bandung

## Membaca, Memvisualisasikan Waveform, dan Menghitung Durasi File Audio Menggunakan Python

### Tujuan Pembelajaran
1. Memahami cara membaca file audio menggunakan Python.
2. Mempelajari cara memvisualisasikan waveform dari file audio.
3. Menghitung durasi file audio menggunakan pustaka **Librosa** dan **Scipy**.

### Alat dan Bahan
1. **Python 3.x** dengan pustaka berikut telah terinstal:
   - Librosa: `pip install librosa`
   - Scipy: `pip install scipy`
   - Matplotlib: `pip install matplotlib`
   - NumPy: `pip install numpy`
2. File audio dalam format **WAV** atau **MP3** untuk diuji coba.

---

## 1. Membaca dan Menampilkan Waveform

Waveform adalah representasi visual dari amplitudo sinyal audio sepanjang waktu. Kita dapat menggunakan **Librosa** untuk membaca file audio dan **Matplotlib** untuk menampilkannya.

```python
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Membaca file audio
file_audio = 'audio_example.wav'
y, sr = librosa.load(file_audio, sr=None)  # sr=None mempertahankan sample rate asli

# Menampilkan waveform
plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform Audio")
plt.xlabel("Waktu (detik)")
plt.ylabel("Amplitudo")
plt.show()
```

---

## 2. Menghitung Durasi File Audio

Durasi audio dapat dihitung dengan membagi jumlah sampel dengan sample rate. Berikut adalah implementasi menggunakan **Librosa** dan **Scipy**:

```python
import librosa
import scipy.io.wavfile

# Menggunakan Librosa
y, sr = librosa.load('audio_example.wav', sr=None)
duration_librosa = librosa.get_duration(y=y, sr=sr)
print(f"Durasi (Librosa): {duration_librosa:.2f} detik")

# Menggunakan Scipy
sr_scipy, y_scipy = scipy.io.wavfile.read('audio_example.wav')
duration_scipy = len(y_scipy) / sr_scipy
print(f"Durasi (Scipy): {duration_scipy:.2f} detik")
```

---

## Diskusi
1. Apa keunggulan dan kelemahan menggunakan **Librosa** dibandingkan **Scipy** dalam membaca file audio?
2. Mengapa penting untuk menampilkan waveform dalam analisis audio?
3. Bagaimana perubahan **sample rate** mempengaruhi representasi waveform?
4. Apa dampak **noise** dalam waveform, dan bagaimana cara menguranginya?
5. Bagaimana metode lain yang bisa digunakan untuk mengukur durasi file audio selain yang disebutkan di atas?

---

## Tugas
1. Uji coba membaca file audio dengan berbagai format (**WAV, MP3**) dan bandingkan hasilnya.
2. Eksperimen dengan berbagai **sample rate** saat membaca file audio menggunakan **Librosa**.
3. Coba visualisasikan waveform dari berbagai jenis audio (**musik, suara manusia, suara lingkungan**) dan analisis perbedaannya.
4. Bandingkan durasi yang dihitung oleh **Librosa** dan **Scipy** untuk beberapa file audio yang berbeda.
5. Terapkan filter untuk menghilangkan **noise** dari waveform dan analisis efeknya.

---

**Selesai!**