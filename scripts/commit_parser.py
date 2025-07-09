import subprocess

def get_changed_files():
    try:
        # Try getting changed files from last commit
        result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], capture_output=True, text=True)
        changed_files = result.stdout.splitlines()

        # If no changes found, list all tracked files
        if not changed_files:
            print("No changes found using git diff. Listing all files instead.")
            result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True)
            changed_files = result.stdout.splitlines()

        for file in changed_files:
            print(file)

    except Exception as e:
        print(f"Error getting changed files: {e}")

if __name__ == "__main__":
    get_changed_files()
