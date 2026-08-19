from nero.voice.voice_engine import VoiceEngine
from nero.brain.command_normalizer import CommandNormalizer
from nero.brain.intent_router import IntentRouter
from nero.automation.executor import NeroExecutor


def main():

    print("================================")
    print("        NERO AI AGENT")
    print("================================")
    print("NERO is starting...")
    print()

    voice = VoiceEngine()
    normalizer = CommandNormalizer()
    router = IntentRouter()
    executor = NeroExecutor()

    print()
    print("NERO is ready.")
    print("Say 'NERO, shut down' to exit.")
    print("--------------------------------")

    while True:

        # Listen
        command = voice.listen()

        if not command:
            print("NERO: I didn't hear a command.")
            print("--------------------------------")
            continue

        print()
        print(f"You said: {command}")

        # Normalize
        normalized_command = normalizer.normalize(command)

        if not normalized_command:
            print("NERO: I didn't hear a command.")
            print("--------------------------------")
            continue

        print(f"NERO normalized: {normalized_command}")

        # Route
        result = router.route(normalized_command)

        route = result["route"]

        # System commands
        if route == "system":

            task = result["task"]

            if task["intent"] == "shutdown":
                print("NERO: Shutting down.")
                break

        # Fast commands
        elif route == "fast":

            task = result["task"]

            print()
            print(f"Fast task: {task}")

            response = executor.execute(task)

            print()
            print(f"NERO: {response}")

        # AI commands
        elif route == "ai":

            print()
            print("NERO: This task requires AI reasoning.")
            print(f"Command: {result['command']}")

        print("--------------------------------")


if __name__ == "__main__":
    main()