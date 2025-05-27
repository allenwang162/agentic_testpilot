import time
import sys  # ✅ Required for sys.stdout
import logging
import structlog
import requests
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up structured logger
logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)
logger = structlog.wrap_logger(logging.getLogger(), processors=[structlog.processors.JSONRenderer()])


def click_button(driver, testid):
    btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-testid="{testid}"]'))
    )
    btn.click()

def get_result(driver):
    def result_not_default(driver):
        text = driver.find_element(By.ID, "current-operand").text.strip()
        return text not in ["", "0"]

    WebDriverWait(driver, 5).until(result_not_default)
    return driver.find_element(By.ID, "current-operand").text.strip()

def clear_calculator(driver):
    click_button(driver, "clear-btn")

# --- Addition Test Cases ---
def test_add_3_plus_2(driver):
    test_name = "test_add_3_plus_2"
    log_event = {}
    try:
        clear_calculator(driver)
        click_button(driver, "number-3")
        click_button(driver, "add-btn")
        click_button(driver, "number-2")
        click_button(driver, "equals-btn")
        assert get_result(driver) == "5"
        log_event = {"event": "test_passed", "test": test_name, "result": "5"}
    except Exception as e:
        log_event = {"event": "test_failed", "test": test_name, "error": str(e)}
        raise

def test_add_10_plus_15(driver):
    test_name = "test_add_10_plus_15"
    log_event = {}
    try:
        clear_calculator(driver)
        click_button(driver, "number-1")
        click_button(driver, "number-0")
        click_button(driver, "add-btn")
        click_button(driver, "number-1")
        click_button(driver, "number-5")
        click_button(driver, "equals-btn")
        assert get_result(driver) == "25"
        log_event = {"event": "test_passed", "test": test_name, "result": "25"}
    except Exception as e:
        log_event = {"event": "test_failed", "test": test_name, "error": str(e)}
        raise

def test_add_negative_numbers(driver):
    test_name = "test_add_negative_numbers"
    log_event = {}
    try:
        clear_calculator(driver)
        click_button(driver, "subtract-btn")
        click_button(driver, "number-5")
        click_button(driver, "add-btn")
        click_button(driver, "subtract-btn")
        click_button(driver, "number-3")
        click_button(driver, "equals-btn")
        assert get_result(driver) == "-8"
        log_event = {"event": "test_passed", "test": test_name, "result": "-8"}
    except Exception as e:
        log_event = {"event": "test_failed", "test": test_name, "error": str(e)}
        raise

# --- Subtraction Test Cases ---
def test_subtract_7_minus_5(driver):
    test_name = "test_subtract_7_minus_5"
    log_event = {}
    try:
        clear_calculator(driver)
        click_button(driver, "number-7")
        click_button(driver, "subtract-btn")
        click_button(driver, "number-5")
        click_button(driver, "equals-btn")
        assert get_result(driver) == "2"
        log_event = {"event": "test_passed", "test": test_name, "result": "2"}
    except Exception as e:
        log_event = {"event": "test_failed", "test": test_name, "error": str(e)}
        raise

def test_subtract_20_minus_30(driver):
    test_name = "test_subtract_20_minus_30"
    log_event = {}
    try:
        clear_calculator(driver)
        click_button(driver, "number-2")
        click_button(driver, "number-0")
        click_button(driver, "subtract-btn")
        click_button(driver, "number-3")
        click_button(driver, "number-0")
        click_button(driver, "equals-btn")
        assert get_result(driver) == "-10"
        log_event = {"event": "test_passed", "test": test_name, "result": "-10"}
    except Exception as e:
        log_event = {"event": "test_failed", "test": test_name, "error": str(e)}
        raise

def test_subtract_negative_numbers(driver):
    test_name = "test_subtract_negative_numbers"
    log_event = {}
    try:
        clear_calculator(driver)
        click_button(driver, "subtract-btn")
        click_button(driver, "number-8")
        click_button(driver, "subtract-btn")
        click_button(driver, "subtract-btn")
        click_button(driver, "number-2")
        click_button(driver, "equals-btn")
        assert get_result(driver) == "-6"
        log_event = {"event": "test_passed", "test": test_name, "result": "-6"}
    except Exception as e:
        log_event = {"event": "test_failed", "test": test_name, "error": str(e)}
        raise
