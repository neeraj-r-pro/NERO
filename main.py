from nero.voice.voice_engine import VoiceEngine
from nero.brain.nero_brain import NeroBrain
from nero.automation.executor import NeroExecutor


def main():

    print("================================")
    print("        NERO AI AGENT")
    print("================================")
    print("NERO is starting...")
    print()

    voice = VoiceEngine()
    brain = NeroBrain()
    executor = NeroExecutor()

    print()
    print("NERO is ready.")
    print("Say 'NERO, shut down' to exit.")
    print("--------------------------------")

    while True:

        command = voice.listen()

        # No speech detected
        if not command:
            print("NERO: I didn't hear a command.")
            print("--------------------------------")
            continue

        print()
        print(f"You said: {command}")

        # Exit command
        command_lower = command.lower()

        if "shut down" in command_lower or "shutdown" in command_lower:
            print("NERO: Shutting down.")
            break

        # Understand command
        task = brain.understand(command)

        print()
        print(f"NERO task: {task}")

        # Execute task
        result = executor.execute(task)

        print()
        print(f"NERO: {result}")
        print("--------------------------------")


if __name__ == "__main__":
    main()