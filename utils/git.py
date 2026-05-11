import subprocess
from pathlib import Path

def init_git(project_path: Path):
    subprocess.run(
    ["git", "init", "-b", "main"],
    cwd=project_path
    )

def git_ignore(project_path: Path):

    gitignore = project_path / ".gitignore"

    gitignore.write_text(
    "venv/\n"
    "__pycache__/\n"
    ".env\n"
    )

