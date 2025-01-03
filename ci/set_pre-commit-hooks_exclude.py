import os
import re

from ruamel.yaml import YAML


def extract_folders(directory: str) -> str:
    """Extract folders and file names under the site folder automatically generated by mkdocs

    Args:
        directory (str): Target Folder Name

    Returns:
        str: Returns a concatenated string of folder and file names under the specified folder
    """
    exclude_pattern = ""
    folder_paths = []
    for root, dirs, _ in os.walk(directory):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            folder_paths.append(folder_path)

    if folder_paths:
        folder_paths.insert(0, directory)
        pattern = "|".join(map(re.escape, folder_paths))
        exclude_pattern = f"({pattern})/.*"

    return exclude_pattern


def add_exclude_pattern_to_yaml(yaml_file: str, exclude_pattern: str) -> None:
    """Sets the "exclude" key at element 0,1 of the "hooks" key in the "repo" list of the "repos" key

    Args:
        yaml_file (str): YAML file name
        exclude_pattern (str): a concatenated string of folder and file names under the specified folder
    """
    yaml = YAML()
    yaml.indent(sequence=4, offset=2)
    # Set to keep quotation marks
    yaml.preserve_quotes = True

    with open(yaml_file, "r") as f:
        data = yaml.load(f)

    # Remove single quotes, if any.
    exclude_pattern = exclude_pattern.replace("'", "")

    # Setting the exclude pattern
    # - id: trailing-whitespace
    if "exclude" in data["repos"][0]["hooks"][0]:
        data["repos"][0]["hooks"][0]["exclude"] = exclude_pattern
    else:
        data["repos"][0]["hooks"][0]["exclude"] = ""

    # - id: end-of-file-fixer
    if "exclude" in data["repos"][0]["hooks"][1]:
        data["repos"][0]["hooks"][1]["exclude"] = exclude_pattern
    else:
        data["repos"][0]["hooks"][1]["exclude"] = ""

    with open(yaml_file, "w") as f:
        yaml.dump(data, f)


if __name__ == "__main__":
    exclude_pattern = extract_folders("site")
    # If exclude is undefined, initialize with single quote
    # Override with exclude_pattern if already defined
    add_exclude_pattern_to_yaml(".pre-commit-config.yaml", exclude_pattern)
    # Override with exclude_pattern
    add_exclude_pattern_to_yaml(".pre-commit-config.yaml", exclude_pattern)
