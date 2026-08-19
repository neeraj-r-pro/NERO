import re


class CommandNormalizer:

    def __init__(self):
        print("NERO Command Normalizer initialized.")

    def normalize(self, command):

        if not command:
            return ""

        command = command.lower().strip()

        # Remove punctuation
        command = re.sub(r"[^\w\s]", " ", command)

        # Normalize whitespace
        command = re.sub(r"\s+", " ", command).strip()

        # Common Whisper variations of "NERO"
        nero_variations = [
            "narrow",
            "niro",
            "near",
            "neero",
            "hero",
            "mirror",
            "nero"
        ]

        for variation in nero_variations:

            command = re.sub(
                rf"\b{variation}\b",
                "nero",
                command
            )

        # Common application recognition variations
        replacements = {

            # Chrome
            "crawl": "chrome",
            "curl": "chrome",
            "chrome browser": "chrome",

            # Notepad
            "not bad": "notepad",
            "note pad": "notepad",
            "not bad app": "notepad",

            # YouTube
            "you tube": "youtube",

        }

        for wrong, correct in replacements.items():

            command = re.sub(
                rf"\b{re.escape(wrong)}\b",
                correct,
                command
            )

        # Remove wake word wherever it appears
        command = re.sub(
            r"\bnero\b",
            "",
            command
        )

        # Remove common filler words
        command = re.sub(
            r"\b(please|can you|could you|would you|hello)\b",
            "",
            command
        )

        # Normalize whitespace again
        command = re.sub(
            r"\s+",
            " ",
            command
        ).strip()

        return command


if __name__ == "__main__":

    normalizer = CommandNormalizer()

    test_commands = [
        "NERO, open Chrome.",
        "narrow open chrome",
        "Niro, launch the browser",
        "mirror open chrome",
        "little open not bad",
        "Niro, open, curl",
        "find a python tutor on youtube",
        "near",
        "Hello, Nero, please open Chrome",
    ]

    print()
    print("================================")
    print("   NERO NORMALIZER TEST")
    print("================================")

    for command in test_commands:

        result = normalizer.normalize(command)

        print()
        print(f"Input : {command}")
        print(f"Output: {result}")