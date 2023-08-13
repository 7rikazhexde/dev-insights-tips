#!.venv/bin/python3

import subprocess


def git_add_if_diff(directory: str) -> None:
    """Run the git diff command to see if there are any differences

    Args:
        directory (str): directory name
    """
    result = subprocess.run(
        ["git", "diff", "--quiet", "--exit-code", directory], capture_output=True
    )

    if result.returncode != 0:
        # If there is a difference, run the git add command
        subprocess.run(["git", "add", directory])
        print(f"{__file__}: git add {directory}")
    else:
        print(f"{__file__}: There is no difference in {directory}")


# mkdocs build
if __name__ == "__main__":  # pragma: no cover
    # Note: "poetry run pre-commit run --all-files" will result in Failed
    # subprocess.run(["poetry", "run", "mkdocs", "build", "--clean"])
    # subprocess.run(["poetry", "run", "task", "mkmb"])

    # Execute in the following format
    subprocess.run(["mkdocs", "build", "--clean"])
    git_add_if_diff("site")
