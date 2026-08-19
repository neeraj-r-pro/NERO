# Actions that NERO's AI is currently allowed to request.

ALLOWED_ACTIONS = {
    "open_application",
    "close_application",
    "open_url",
    "browser_search",
    "wait",
}


def is_allowed_action(action):
    return action in ALLOWED_ACTIONS


def validate_action(action_data):

    if not isinstance(action_data, dict):
        return False, "Action must be an object."

    action = action_data.get("action")

    if not action:
        return False, "Missing action."

    if not is_allowed_action(action):
        return False, f"Action '{action}' is not allowed."

    return True, "Action is valid."


def validate_plan(plan):

    if not isinstance(plan, dict):
        return False, "Plan must be an object."

    if "goal" not in plan:
        return False, "Plan is missing a goal."

    actions = plan.get("actions")

    if not isinstance(actions, list):
        return False, "Plan actions must be a list."

    if not actions:
        return False, "Plan contains no actions."

    for action in actions:

        valid, message = validate_action(action)

        if not valid:
            return False, message

    return True, "Plan is valid."


if __name__ == "__main__":

    test_plan = {
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

    valid, message = validate_plan(test_plan)

    print("Valid:", valid)
    print("Message:", message)