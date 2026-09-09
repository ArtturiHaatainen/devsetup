from devsetup.utils.environment import check_git, check_node, check_python,detect_os

def run_doctor():
    checks = [
        check_git(),
        check_python(),
        check_node(),
        detect_os()
    ]

    for check in checks:
        print(check)