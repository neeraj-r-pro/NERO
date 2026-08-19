import time

import numpy as np
import sounddevice as sd


SAMPLE_RATE = 16000
CHANNELS = 1
CHUNK_SIZE = 1600
DEVICE = 1


def calculate_volume(audio):
    audio = np.asarray(audio)

    if audio.size == 0:
        return 0.0

    return float(np.sqrt(np.mean(audio ** 2)))


print("================================")
print("      NERO MICROPHONE TEST")
print("================================")
print()
print("Speak normally for 5 seconds.")
print("Watch the volume values.")
print()

time.sleep(2)

with sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    dtype="float32",
    blocksize=CHUNK_SIZE,
    device=DEVICE
) as stream:

    start = time.time()

    while time.time() - start < 5:

        audio, overflowed = stream.read(CHUNK_SIZE)

        volume = calculate_volume(audio)

        print(f"Volume: {volume:.5f}")

print()
print("Microphone test complete.")