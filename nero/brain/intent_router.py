import re


class IntentRouter:

    def __init__(self):
        print("NERO Intent Router initialized.")

    def normalize(self, command):
        """
        Normalize common speech-recognition variations.
        """

        command = command.lower().strip()

        # Common Whisper variations of "NERO"
        command = re.sub(
            r"\b(narrow|near|nero|niro|hero)\b",
            "nero",
            command
        )

        # Remove wake word
        command = re.sub(
            r"^\s*nero[\s,;:.-]*",
            "",
            command
        )

        return command.strip()

    def route(self, command):

        command = self.normalize(command)

        # Open Chrome
        if (
            re.search(r"\b(open|launch|start)\b", command)
            and re.search(r"\b(chrome|browser)\b", command)
        ):
            return {
                "route": "fast",
                "task": {
                    "intent": "open_application",
                    "target": "chrome"
                }
            }

        # Open Notepad
        if (
            re.search(r"\b(open|launch|start)\b", command)
            and re.search(r"\bnotepad\b", command)
        ):
            return {
                "route": "fast",
                "task": {
                    "intent": "open_application",
                    "target": "notepad"
                }
            }

        # Shutdown
        if re.search(
            r"\b(shut\s*down|shutdown|exit|quit)\b",
            command
        ):
            return {
                "route": "system",
                "task": {
                    "intent": "shutdown"
                }
            }

        # Unknown / complex command
        return {
            "route": "ai",
            "task": None,
            "command": command
        }


if __name__ == "__main__":

    router = IntentRouter()

    while True:

        command = input("\nCommand: ")

        if command.lower() == "test":
            break

        result = router.route(command)

        print("Router result:")
        print(result)