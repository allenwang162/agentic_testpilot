import os

def fetch_testing_requirements(requirement_filename):
    req_path = os.path.join(os.path.dirname(__file__), "..", "testdata", requirement_filename)
    try:
        with open(req_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Requirements file '{requirement_filename}' not found in testdata folder."