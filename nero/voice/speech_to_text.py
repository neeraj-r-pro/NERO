from faster_whisper import WhisperModel


MODEL_SIZE = "base.en"


def transcribe_audio(audio_file):
    print("Loading Whisper model...")

    model = WhisperModel(
        MODEL_SIZE,
        device="cpu",
        compute_type="int8"
    )

    print("Transcribing audio...")

    segments, info = model.transcribe(
        audio_file,
        beam_size=5
    )

    text = " ".join(segment.text for segment in segments)

    return text.strip()


if __name__ == "__main__":
    audio_file = "data/test_recording.wav"

    result = transcribe_audio(audio_file)

    print()
    print("================================")
    print("       NERO TRANSCRIPTION")
    print("================================")
    print(f"You said: {result}")