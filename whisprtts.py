import whisper
from whisper_mic import WhisperMic

model = whisper.load_model("turbo")
mic = WhisperMic
result = model.transcribe("audio.mp3")
print(result["text"])
