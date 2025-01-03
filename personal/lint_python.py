import os
import subprocess


def get_python_files(directory):
    """Recursively find all Python files in the given directory."""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def lint_files(files):
    """Run flake8 on a list of Python files."""
    for file in files:
        try:
            print(f"Linting: {file}")
            result = subprocess.run(
                ["flake8", file],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"No issues found in {file}")
            else:
                print(f"Issues in {file}:\n{result.stdout}")
        except Exception as e:
            print(f"Error linting {file}: {e}")


if __name__ == "__main__":
    """Entry point for the script."""
    # Set the directory to lint
    directory_to_lint = "./"  # Change this to your project's root directory
    python_files = get_python_files(directory_to_lint)
    if not python_files:
        print("No Python files found to lint.")
    else:
        lint_files(python_files)
