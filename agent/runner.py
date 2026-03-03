import subprocess
from agent.failure_parser import extract_assertion_failure
from agent.fixer import generate_fix
from agent.github_client import create_pr

def run_tests():
    result = subprocess.run(
        ["pytest", "-v"],
        capture_output=True,
        text=True
    )
    return result.stdout

def run_agent():
    output = run_tests()

    if "FAILED" not in output:
        print("No failures detected.")
        return

    failure = extract_assertion_failure(output)

    if not failure:
        print("No supported failure pattern found.")
        return

    fix = generate_fix()

    create_pr(fix["correct_userId"])