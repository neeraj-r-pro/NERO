import json
import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:4b"


class LLMBrain:

    def __init__(self):
        print("NERO LLM Brain initialized.")

    def think(self, command):

        system_prompt = """
You are NERO, a Windows computer AI agent.

Your job is to convert the user's natural-language command
into a structured action plan.

Return ONLY valid JSON.

Use this format:

{
    "goal": "short description of the goal",
    "actions": [
        {
            "action": "action_name",
            "target": "target",
            "value": "optional value"
        }
    ]
}

Do not include markdown.
Do not include explanations.
Do not include reasoning.
"""

        payload = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": command
                }
            ],
            "stream": False
        }

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        content = data["message"]["content"]

        return content


if __name__ == "__main__":

    brain = LLMBrain()

    command = input("Enter a command for NERO: ")

    result = brain.think(command)

    print()
    print("================================")
    print("          NERO BRAIN")
    print("================================")
    print(result)