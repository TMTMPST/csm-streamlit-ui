import os
from generator.generator import load_csm_1b, Segment
from huggingface_hub import hf_hub_download
import torchaudio
import torch

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

generator = load_csm_1b(device=device)

speakers = [0, 0, 0, 0, 0]
transcripts = [
    "I think it's a good idea to have the reload there because sometimes in movies sometimes they don't reload.",
    "No BGM, just silence. Just me and my voice alone. I am sorry.",
    "Hunt the symbol? What does that even mean? I mean, I don't know. English speakers, help me out here. What's hunt the symbol?",
    "But surely they're not going to be shooting in this train. It's packed with people. Surely, they won't be shooting here.",
    "Hell yeah, we'll keep doing what we always do. Yeah, boys!",
]
audio_paths = [
    "data/A1 (Neutral).wav",
    "data/A2 (Soft).wav",
    "data/A3 (Confused).wav",
    "data/A4 (Sarcastic).wav",
    "data/A5 (Proud).wav",
]

def load_audio(audio_path):
    audio_tensor, sample_rate = torchaudio.load(audio_path)
    if audio_tensor.dim() > 1:
        audio_tensor = torch.mean(audio_tensor, dim=0, keepdim=True)

    audio_tensor = torchaudio.functional.resample(
        audio_tensor.squeeze(), orig_freq=sample_rate, new_freq=generator.sample_rate
    )
    return audio_tensor

segments = [
    Segment(text=transcript, speaker=speaker, audio=load_audio(audio_path))
    for transcript, speaker, audio_path in zip(transcripts, speakers, audio_paths)
]
audio = generator.generate(
    text="Helloooo Vidi, I was ..... Missing you",
    speaker=0,
    context=segments,
    max_audio_length_ms=30_000,  # Increased processing time
    temperature=0.7,  # Controls randomness
)

torchaudio.save("audio.wav", audio.unsqueeze(0).cpu(), generator.sample_rate)