# THis version of the program saves your audio as an individual file for later use. it runs one time, which means you'll have to run whisprtts.py again to make another TTS output
# You'll have to install phonemizer tts and espeak-ng for this to work.
# to install both of these, run these commands in your terminal:
# pip install phonemizer TTS
# sudo apt install espeak-ng

import os
from phonemizer import phonemize
from TTS.api import TTS

input_file = "outputtranscriptSF.txt"
phoneme_txt = "outputphonemesSF.txt"
output_audio_file = "phonemizeraudio.wav"

os.makedirs("recordings", exist_ok=True)

with open(input_file, "r") as file:
    transcript = file.read().strip()

print("Transcript:", transcript)


phonemes = phonemize(transcript, language='en-us', backend='espeak', strip=True)

with open(phoneme_txt, "w") as file:
    file.write(phonemes)

print("Phonemes saved:", phoneme_txt)
print(phonemes)
print("\nLoading TTS...")
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

tts.tts_to_file(text=phonemes, file_path=output_audio_file)
print("\nAudio saved:", output_audio_file)
