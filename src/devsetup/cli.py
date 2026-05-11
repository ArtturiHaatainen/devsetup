import sys
from devsetup.commands.create import create_project
from devsetup.commands.doctor import run_doctor

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 main.py create <name>")
        print("  python3 main.py doctor")
        return

    command = sys.argv[1]

    if command == "create":
        if len(sys.argv) < 3:
            print("Missing project name")
            return

        project_name = sys.argv[2]
        create_project(project_name)

    elif command == "doctor":
        run_doctor()

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()