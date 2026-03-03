import re

def extract_assertion_failure(pytest_output):
    pattern = r"assert (.+) == (.+)"
    match = re.search(pattern, pytest_output)

    if match:
        return {
            "left": match.group(1),
            "right": match.group(2)
        }
    return None