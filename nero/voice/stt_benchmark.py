import time

from faster_whisper import WhisperModel


AUDIO_FILE = "data/command.wav"
MODEL_SIZE = "tiny.en"


print("Loading Whisper...")

start = time.perf_counter()

model = WhisperModel(
    MODEL_SIZE,
    device="cpu",
    compute_type="int8"
)

load_time = time.perf_counter() - start

print(f"Model load time: {load_time:.2f} seconds")
print("Transcribing...")

start = time.perf_counter()

segments, info = model.transcribe(
    AUDIO_FILE,
    beam_size=1,
    vad_filter=True
)

text = " ".join(
    segment.text for segment in segments
).strip()

transcription_time = time.perf_counter() - start

print()
print("================================")
print("       NERO STT BENCHMARK")
print("================================")
print(f"Text: {text}")
print(f"Transcription time: {transcription_time:.2f} seconds")
print(f"Audio duration: {info.duration:.2f} seconds")