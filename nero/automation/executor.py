import os
import subprocess
import webbrowser


class NeroExecutor:

    def __init__(self):
        print("NERO Executor initialized.")

    def execute(self, task):

        intent = task.get("intent")
        target = task.get("target")

        if intent == "open_application":

            if target == "browser":
                webbrowser.open("https://www.google.com")
                return "Browser opened."

            if target == "chrome":
                self.open_chrome()
                return "Chrome opened."

            if target == "notepad":
                subprocess.Popen("notepad.exe")
                return "Notepad opened."

        return "I don't know how to perform that task yet."

    def open_chrome(self):

        possible_paths = [
            os.path.expandvars(
                r"%PROGRAMFILES%\Google\Chrome\Application\chrome.exe"
            ),
            os.path.expandvars(
                r"%PROGRAMFILES(X86)%\Google\Chrome\Application\chrome.exe"
            ),
            os.path.expandvars(
                r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
            )
        ]

        for path in possible_paths:

            if os.path.exists(path):
                subprocess.Popen([path])
                return

        # Fallback
        webbrowser.open("https://www.google.com")


if __name__ == "__main__":

    executor = NeroExecutor()

    test_task = {
        "intent": "open_application",
        "target": "chrome"
    }

    result = executor.execute(test_task)

    print(result)