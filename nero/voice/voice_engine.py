import time

import numpy as np
import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel


SAMPLE_RATE = 16000
CHANNELS = 1
AUDIO_FILE = "data/command.wav"

MODEL_SIZE = "tiny.en"

# Voice detection settings
CALIBRATION_DURATION = 1.0
CHUNK_DURATION = 0.1

SILENCE_DURATION = 1.2
MAX_RECORDING_DURATION = 15.0

# Minimum time to record after speech begins
MIN_SPEECH_DURATION = 0.4

# How much louder speech should be than background noise
THRESHOLD_MULTIPLIER = 1.5


class VoiceEngine:

    def __init__(self):

        print("Loading NERO speech engine...")

        self.model = WhisperModel(
            MODEL_SIZE,
            device="cpu",
            compute_type="int8"
        )

        print("Speech engine ready.")

    def calculate_volume(self, audio):

        audio = np.asarray(audio)

        if audio.size == 0:
            return 0.0

        return float(np.sqrt(np.mean(audio ** 2)))

    def calibrate_microphone(self):

        print("Calibrating microphone...")

        calibration = sd.rec(
            int(CALIBRATION_DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="float32",
            device=1
        )

        sd.wait()

        noise_level = self.calculate_volume(calibration)

        threshold = max(
            noise_level * THRESHOLD_MULTIPLIER,
            0.0005
        )

        print(f"Background level: {noise_level:.4f}")
        print(f"Voice threshold: {threshold:.4f}")

        return threshold

    def record(self):

        threshold = self.calibrate_microphone()

        chunk_size = int(CHUNK_DURATION * SAMPLE_RATE)

        print()
        print("NERO is listening...")
        print("Speak now!")

        audio_chunks = []

        speech_started = False
        speech_start_time = None
        silence_start_time = None

        start_time = time.time()

        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="float32",
            blocksize=chunk_size,
            device=1
        ) as stream:

            while True:

                audio, overflowed = stream.read(chunk_size)

                audio = np.asarray(audio).copy()

                volume = self.calculate_volume(audio)

                current_time = time.time()

                # Prevent NERO from listening forever
                if current_time - start_time > MAX_RECORDING_DURATION:
                    break

                # Speech detected
                if volume >= threshold:

                    if not speech_started:

                        speech_started = True
                        speech_start_time = current_time

                        print("Speech detected.")

                    silence_start_time = None

                    audio_chunks.append(audio)

                # Silence
                elif speech_started:

                    audio_chunks.append(audio)

                    if silence_start_time is None:
                        silence_start_time = current_time

                    if (
                        current_time - silence_start_time
                        >= SILENCE_DURATION
                    ):
                        break

        # No speech detected
        if not speech_started:

            print("No speech detected.")

            return False

        speech_duration = time.time() - speech_start_time

        if speech_duration < MIN_SPEECH_DURATION:

            print("Speech was too short.")

            return False

        audio_data = np.concatenate(audio_chunks)

        sf.write(
            AUDIO_FILE,
            audio_data,
            SAMPLE_RATE
        )

        print("Recording complete.")

        return True

    def transcribe(self):

        print("Understanding...")

        segments, info = self.model.transcribe(
            AUDIO_FILE,
            beam_size=1,
            vad_filter=True
        )

        text = " ".join(
            segment.text for segment in segments
        )

        return text.strip()

    def listen(self):

        recorded = self.record()

        if not recorded:
            return ""

        command = self.transcribe()

        return command


if __name__ == "__main__":

    nero_voice = VoiceEngine()

    command = nero_voice.listen()

    print()
    print("================================")
    print("          NERO HEARD")
    print("================================")

    if command:
        print(f"You said: {command}")
    else:
        print("NERO did not hear a command.")