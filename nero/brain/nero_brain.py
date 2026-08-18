class NeroBrain:

    def __init__(self):
        print("NERO Brain initialized.")

    def understand(self, command):
        command = command.lower().strip()

        if "open" in command and "browser" in command:
            return {
                "intent": "open_application",
                "target": "browser"
            }

        if "open" in command and "chrome" in command:
            return {
                "intent": "open_application",
                "target": "chrome"
            }

        if "open" in command and "notepad" in command:
            return {
                "intent": "open_application",
                "target": "notepad"
            }

        return {
            "intent": "unknown",
            "target": None
        }


if __name__ == "__main__":

    brain = NeroBrain()

    command = input("Enter a command for NERO: ")

    result = brain.understand(command)

    print()
    print("NERO understood:")
    print(result)