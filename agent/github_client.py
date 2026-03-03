import os
from github import Github

def create_pr(new_value):
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY")

    g = Github(token)
    repo = g.get_repo(repo_name)

    base_branch = repo.get_branch("main")
    new_branch_name = "agent-fix-userid"

    repo.create_git_ref(
        ref=f"refs/heads/{new_branch_name}",
        sha=base_branch.commit.sha
    )

    file = repo.get_contents("tests/test_simple_get_request.py", ref="main")

    updated_content = file.decoded_content.decode().replace(
        'assert data["userId"] == 999',
        f'assert data["userId"] == {new_value}'
    )

    repo.update_file(
        path=file.path,
        message="Agent fix: update userId assertion",
        content=updated_content,
        sha=file.sha,
        branch=new_branch_name
    )

    repo.create_pull(
        title="AI Suggested Fix: Update userId Assertion",
        body="Automated fix generated based on API response.",
        head=new_branch_name,
        base="main"
    )