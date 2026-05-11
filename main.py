from pathlib import Path
from utils.git import init_git, git_ignore

project_name = input("Project name: ")

project_path = Path(project_name)

project_path.mkdir()

print(f"Created project: {project_name}")

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

readme.write_text(content)


init_git(project_path)
git_ignore(project_path)