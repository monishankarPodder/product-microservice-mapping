import json
import sys
import re

def load_testcases(json_path):
    with open(json_path, 'r') as file:
        return json.load(file)

def split_keywords(text):
    # Split camelCase or PascalCase words, remove file extension
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', text)
    return [word.lower() for word in words]

def map_tests(changed_files, testcases):
    keywords = []
    for file in changed_files:
        filename = file.split('/')[-1].split('.')[0]  # Get file name without extension
        keywords.extend(split_keywords(filename))     # Split into separate words

    suggested = []

    for testcase in testcases:
        tc_name = testcase.get("name", "").lower()
        tc_folder = testcase.get("folder", "").lower()

        if any(keyword in tc_name or keyword in tc_folder for keyword in keywords):
            suggested.append(testcase.get("name"))

    return suggested

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        changed_files = [line.strip() for line in f.readlines()]

    testcases = load_testcases(sys.argv[2])
    suggested_tests = map_tests(changed_files, testcases)

    for test in suggested_tests:
        print(test)
