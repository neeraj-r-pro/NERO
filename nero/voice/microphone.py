import sounddevice as sd
import soundfile as sf


SAMPLE_RATE = 16000
DURATION = 5
OUTPUT_FILE = "data/test_recording.wav"


def record_audio():
    print("================================")
    print("       NERO VOICE TEST")
    print("================================")
    print()
    print("NERO is listening...")
    print("Speak now!")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        device=1
    )

    sd.wait()

    sf.write(
        OUTPUT_FILE,
        audio,
        SAMPLE_RATE
    )

    print()
    print(f"Recording saved to: {OUTPUT_FILE}")
    print("NERO finished listening.")


if __name__ == "__main__":
    record_audio()