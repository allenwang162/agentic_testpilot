import os

def save_ui_test_case(openai_response_path: str) -> None:
    """
    Appends the content of the OpenAI response file to the end of tests/test_ui.py.
    """

    test_file_path = os.path.join(os.path.dirname(__file__), "..", "tests", "test_ui.py")
    with open(openai_response_path, "r", encoding="utf-8") as resp_file:
        code = resp_file.read().strip()
    with open(test_file_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + code + "\n")