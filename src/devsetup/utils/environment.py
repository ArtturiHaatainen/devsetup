from dataclasses import dataclass
import shutil
import subprocess
import platform

@dataclass
class CheckResult:
    name: str
    available: bool
    version: str | None = None
def detect_os():
    return platform.system()

def check_git() -> CheckResult:
    git_path = shutil.which("git")

    if git_path is None:
        return CheckResult(
            name="Git",
            available=False
        )  

    result = subprocess.run(
        ["git", "--version"],
        capture_output=True,
        text=True
    )

    version = result.stdout.strip().replace("git version ", "")
    
    return CheckResult(
                name="Git",
                available=True,
                version=version
    )  
        


def check_python() -> CheckResult:
    python_path = shutil.which("python3")

    if python_path is None:
        return CheckResult(
            name="Python",
            available=False
        )  

    result = subprocess.run(
        ["python3", "--version"],
        capture_output=True,
        text=True
    )

    version = result.stdout.strip().replace("Python version ", "")
    
    return CheckResult(
                name="Python",
                available=True,
                version=version
    )  
        


def check_node() -> CheckResult:
    node_path = shutil.which("node")

    if node_path is None:
        return CheckResult(
            name="Node.js",
            available=False
        )

    result = subprocess.run(
        ["node", "--version"],
        capture_output=True,
        text=True
    )

    version = result.stdout.strip().replace("v", "")

    return CheckResult(
        name="Node.js",
        available=True,
        version=version
    )    

