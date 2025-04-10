import librosa
import scipy.io.wavfile as wav

def bandingkan_durasi(nama_file):
    y, sr = librosa.load(nama_file, sr=None)
    dur_librosa = librosa.get_duration(y=y, sr=sr)

    sr_scipy, y_scipy = wav.read(nama_file)
    dur_scipy = len(y_scipy) / sr_scipy

    print(f"{nama_file} => Durasi Librosa: {dur_librosa:.2f} s | Durasi Scipy: {dur_scipy:.2f} s")

bandingkan_durasi("audio1.wav")
bandingkan_durasi("audio2.wav")
bandingkan_durasi("audio3.wav")
