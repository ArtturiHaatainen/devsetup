# DevSetup

DevSetup is a Python-based CLI tool for quickly bootstrapping new development projects in a Linux or WSL environment.

The goal of the project is to automate repetitive setup tasks when starting a new software project, such as creating folder structures, initializing Git repositories, generating common files, and setting up Python virtual environments.

This project was built as a portfolio project to demonstrate:

- Python CLI development
- Packaging with pip
- src-layout project structure
- Developer workflow automation
---

## Features

Current features:

- Create a new project structure
- Generate a README.md file based on the project
- Generate a .gitignore file
- Initialize a Git repository
- Works globally as CLI tool

Planned features:

- FastAPI project templates
- React project templates
- Docker and Docker Compose templates
- VS Code workspace setup
- Environment validation commands
- Configurable project templates
- Doctor mode

---

## Technologies

- Python 3
- Setuptools / pip
- pathlib
- subprocess
- Git
- Linux / WSL

---

## Project Structure

```text
devsetup/
├── src/
│   └── devsetup/
│       ├── cli.py
│       ├── commands/
│       ├── utils/
│       └── templates/
├── pyproject.toml
└── README.md
```
## Requirements
- Python 3
- Git
- pip
- Linux/WSL

## Installation
```
git clone https://github.com/ArtturiHaatainen/devsetup.git (https version)
cd devsetup
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Example usage
```
devsetup create my-project
Project name: my-project
[OK] Folder created
[OK] README created
[OK] Git initialized
[OK] Gitignore created
```