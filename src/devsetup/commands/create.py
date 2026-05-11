from pathlib import Path
from devsetup.utils.git import init_git, create_gitignore
from devsetup.utils.logger import log_ok


def create_project(project_name: str):
    project_name = input("Project name: ")

    project_path = Path(project_name)
        
    try:
        project_path.mkdir()
        log_ok("Folder created")
    except FileExistsError:
        print("Project already exists")
        exit(1)

    readme = project_path / "README.md"

    # Readme content

    content = f"""# {project_name}

## Features

## Installation

## Technologies

## Project Structure

## Requirements

## Example usage
    """

    try:
        readme.write_text(content)
        log_ok("README created")
    except Exception as e:
        print(f"[ERROR] Failed to create README: {e}")
        exit(1)


    init_git(project_path)
    log_ok("Git initialized")

    try:
        create_gitignore(project_path)
        log_ok("Gitignore created")
    except Exception as e:
        print(f"[ERROR] Gitignore failed: {e}")
        exit(1)
