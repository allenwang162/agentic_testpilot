import openai
import os
from datetime import datetime


def generate_ui_tests(requirement, openai_api_key):
    prompt = f"""
Given the following UI requirement, generate pytest UI test cases in Python using Selenium.

Use the following style:

def test_subtract_7_minus_5(driver):
    clear_calculator(driver)
    click_button(driver, "number-7")
    click_button(driver, "subtract-btn")
    click_button(driver, "number-5")
    click_button(driver, "equals-btn")
    assert get_result(driver) == "2"

Requirement:
{requirement}

Generate only the raw Python code for three pytest UI tests that verify calculator operations.
Do NOT include any explanations, markdown formatting, triple backticks, or any text before or after the code.
Only output the Python function code itself, nothing else. nothing like ```python should be included.
"""

    client = openai.OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes Python Selenium UI tests."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=512,
        temperature=0.2,
    )
    response_text = response.choices[0].message.content

    # Save response to response/openai_response_<timestamp>.txt
    response_dir = os.path.join(os.path.dirname(__file__), '..', 'response')
    os.makedirs(response_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    response_path = os.path.join(response_dir, f'openai_response_{timestamp}.txt')
    with open(response_path, 'w', encoding='utf-8') as f:
        f.write(response_text)
    return response_path

# Example usage:
# generate_ui_tests("requirement.txt", "sk-...your-openai-key...")