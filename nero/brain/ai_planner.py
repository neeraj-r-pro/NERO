import json

from nero.brain.action_schema import validate_plan


class AIPlanner:

    def __init__(self):
        print("NERO AI Planner initialized.")

    def parse_plan(self, raw_response):

        try:

            plan = json.loads(raw_response)

        except json.JSONDecodeError:

            return None, "AI returned invalid JSON."

        valid, message = validate_plan(plan)

        if not valid:

            return None, message

        return plan, "Plan is valid."

    def plan(self, command):

        raise NotImplementedError(
            "AI model connection has not been implemented yet."
        )


if __name__ == "__main__":

    planner = AIPlanner()

    test_response = """
    {
        "goal": "Search for Python tutorials",
        "actions": [
            {
                "action": "open_application",
                "target": "chrome"
            },
            {
                "action": "browser_search",
                "query": "Python tutorials"
            }
        ]
    }
    """

    plan, message = planner.parse_plan(test_response)

    print()
    print("================================")
    print("       NERO AI PLANNER")
    print("================================")

    print("Plan:")
    print(plan)

    print()
    print("Result:", message)