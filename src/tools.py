from langchain.tools import tool

from tool_1_fetch_testing_requirements import fetch_testing_requirements
from tool_2_generate_ui_testing_case import generate_ui_tests
from tool_3_save_ui_testing_case import save_ui_test_case
from tool_4_run_ui_testing_case import run_tests_from_file
from tool_5_output_test_result import email_test_output


def get_tools(token: str):
    @tool
    def fetch_requirement_tool(requirement_filename: str) -> str:
        """Fetch testing requirements from a requirement filename."""
        return fetch_testing_requirements(requirement_filename)

    @tool
    def create_test_case_tool(requirement_input: str) -> str:
        """Generate UI test cases from testing case requirements using OpenAI, and produce the testing case."""
        return generate_ui_tests(requirement_input, token)

    @tool
    def save_ui_test_case_tool(test_case_code: str) -> str:
        """Append the given test case code to the end of tests/test_ui.py."""
        save_ui_test_case(test_case_code)
        return "Test case saved to tests/test_ui.py."

    @tool
    def run_pytest_on_file_tool(file_path: str) -> str:
        """Execute pytest on a test file given by its path and return the test result summary."""
        return run_tests_from_file(file_path)

    @tool
    def email_test_output_tool(output_path: str) -> str:
        """Email the test output file to allen.wang@sedgwick.com using iCloud SMTP."""
        return email_test_output(output_path)

    return [fetch_requirement_tool, create_test_case_tool, save_ui_test_case_tool, run_pytest_on_file_tool, email_test_output_tool]