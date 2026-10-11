import sys
import librosa
import torch
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC


MODEL_NAME = "facebook/wav2vec2-xlsr-53-espeak-cv-ft"

processor = Wav2Vec2Processor.from_pretrained(MODEL_NAME)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_NAME)
model.eval()

def hear_phonemes(audio_path):
    audio, _ = librosa.load(audio_path, sr=16000, mono = True)
    inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
    with torch.no_grad():
        logits =model(inputs.input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)


    text = processor.batch_decode(predicted_ids)[0]

    return text.split()



