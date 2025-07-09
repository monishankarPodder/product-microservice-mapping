import subprocess

def get_changed_files():
    result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], capture_output=True, text=True)
    changed_files = result.stdout.splitlines()
    for file in changed_files:
        print(file)

if __name__ == "__main__":
    get_changed_files()
