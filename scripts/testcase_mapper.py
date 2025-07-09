import json
import sys

def load_testcases(json_path):
    with open(json_path, 'r') as file:
        return json.load(file)

def map_tests(changed_files, testcases):
    keywords = [file.split('/')[-1].split('.')[0].lower() for file in changed_files]
    suggested = []

    for testcase in testcases:
        if any(keyword in testcase["name"].lower() or keyword in testcase["folder"].lower() for keyword in keywords):
            suggested.append(testcase["name"])

    return suggested

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        changed_files = [line.strip() for line in f.readlines()]

    testcases = load_testcases(sys.argv[2])
    suggested_tests = map_tests(changed_files, testcases)

    for test in suggested_tests:
        print(test)
