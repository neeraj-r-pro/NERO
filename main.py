from nero.voice.voice_engine import VoiceEngine
from nero.brain.nero_brain import NeroBrain
from nero.automation.executor import NeroExecutor


def main():

    print("================================")
    print("        NERO AI AGENT")
    print("================================")
    print("NERO is starting...")
    print()

    # Initialize NERO components
    voice = VoiceEngine()
    brain = NeroBrain()
    executor = NeroExecutor()

    print()
    print("NERO is ready.")
    print("--------------------------------")

    # Listen for a command
    command = voice.listen()

    print()
    print(f"You said: {command}")

    # Understand the command
    task = brain.understand(command)

    print()
    print(f"NERO task: {task}")

    # Execute the task
    result = executor.execute(task)

    print()
    print(f"NERO: {result}")


if __name__ == "__main__":
    main()