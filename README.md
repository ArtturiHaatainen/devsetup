# DevSetup

DevSetup is a Python-based CLI tool for quickly bootstrapping new development projects in a Linux or WSL environment.

The goal of the project is to automate repetitive setup tasks when starting a new software project, such as creating folder structures, initializing Git repositories, generating common files, and setting up Python virtual environments.

This project was created as a practical portfolio project to improve automation, scripting, and developer workflow skills. Also I wanted to automatize my own development.

---

## Features

Current features:

- Create a new project directory
- Generate a README.md file based on the project
- Generate a .gitignore file
- Initialize a Git repository

Planned features:

- FastAPI project templates
- React project templates
- Docker and Docker Compose templates
- VS Code workspace setup
- Environment validation commands
- Configurable project templates
- Cross-platform support

---

## Technologies

- Python 3
- pathlib
- subprocess
- Git
- Linux / WSL

---

## Project Structure

```text
devsetup/
├── main.py
├── templates/
├── utils/
│   ├── filesystem.py
│   ├── git.py
│   └── python_env.py
└── config/
```
## Requirements
- Python 3
- Git
- Linux/WSL

## Installation
```
git clone https://github.com/ArtturiHaatainen/devsetup.git (https version)
cd devsetup
python3 main.py
```

## Example usage
```
Project name: test

[+] Created project folder
[+] Created README.md
[+] Created .gitignore
[+] Initialized Git repository
[+] Created Python virtual environment
```