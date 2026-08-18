import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel


SAMPLE_RATE = 16000
RECORDING_DURATION = 5
AUDIO_FILE = "data/command.wav"
MODEL_SIZE = "base.en"


class VoiceEngine:

    def __init__(self):
        print("Loading NERO speech engine...")

        self.model = WhisperModel(
            MODEL_SIZE,
            device="cpu",
            compute_type="int8"
        )

        print("Speech engine ready.")

    def record(self):
        print()
        print("NERO is listening...")
        print("Speak now!")

        audio = sd.rec(
            int(RECORDING_DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32",
            device=1
        )

        sd.wait()

        sf.write(
            AUDIO_FILE,
            audio,
            SAMPLE_RATE
        )

        print("Recording complete.")

    def transcribe(self):
        print("Understanding...")

        segments, info = self.model.transcribe(
            AUDIO_FILE,
            beam_size=5
        )

        text = " ".join(
            segment.text for segment in segments
        )

        return text.strip()

    def listen(self):
        self.record()

        command = self.transcribe()

        return command


if __name__ == "__main__":

    nero_voice = VoiceEngine()

    command = nero_voice.listen()

    print()
    print("================================")
    print("          NERO HEARD")
    print("================================")
    print(f"You said: {command}")
    