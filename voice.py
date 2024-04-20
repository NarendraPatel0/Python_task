import pyaudio
import wave
import numpy as np
from pydub import AudioSegment

class VoiceRecorder:
    def __init__(self, output_filename, threshold=500, channels=2, rate=44100, chunk=1024, format=pyaudio.paInt16):
        self.output_filename = output_filename
        self.threshold = threshold
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.format = format
        self.audio = pyaudio.PyAudio()

    def record_audio(self):
        stream = self.audio.open(format=self.format, channels=self.channels,
                                rate=self.rate, input=True,
                                frames_per_buffer=self.chunk)
       
        print("Recording...")

        frames = []
        silent_frames = 0

        while True:
            data = stream.read(self.chunk)
            audio_data = np.frombuffer(data, dtype=np.int16)
            volume = np.max(audio_data)

            # Check if the volume is above the threshold
            if volume < self.threshold:
                silent_frames += 1
                if silent_frames > 100:  # Adjust this number depending on the silence length to end recording
                    break
            else:
                silent_frames = 0

            frames.append(data)
       
        print("Finished recording.")

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        self.audio.terminate()

        # Save the recorded audio
        wf = wave.open(self.output_filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()

        print(f"Audio recorded and saved to {self.output_filename}")

if __name__ == "__main__":
    output_filename = "output.wav"
    recorder = VoiceRecorder(output_filename)
    recorder.record_audio()