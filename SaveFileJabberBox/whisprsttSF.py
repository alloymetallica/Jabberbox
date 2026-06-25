import pyaudio 
import time
import wave
import whisper

model = whisper.load_model("base")

chunk = 1024
format = pyaudio.paInt16
channels = 2
rate = 44100
Output_Filename = "outptSF.wav"
Output_Filename_text = "outputtranscriptSF.txt"
 
p = pyaudio.PyAudio()

stream = p.open(format=format,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=chunk)

frames = []

input("Press ENTER to start recording...")
print("Recording... Press 'CTRL + C' to stop.")

try:
    while True:
        data = stream.read(chunk)
        frames.append(data)
except KeyboardInterrupt:
    print("stopped recording.")
    time.sleep(0.2)

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()

wf = wave.open(Output_Filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Recording saved as {Output_Filename}")
print("Transcribing audio...")


result = model.transcribe(Output_Filename, fp16=False)

text = result["text"]

with open(Output_Filename_text, "w") as f:
    f.write(text)

    print(f"Transcription saved as {Output_Filename_text}")
    print("Transcription:")
    print(text)
