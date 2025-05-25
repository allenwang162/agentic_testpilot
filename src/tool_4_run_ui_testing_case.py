import subprocess
import os
from datetime import datetime

def run_tests_from_file(file_path: str) -> str:
    """
    Run the specified test file using pytest and return results as a string.
    """
    results_dir = os.path.join(os.path.dirname(__file__), '..', 'test_results')
    os.makedirs(results_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"test_output_{timestamp}.txt"
    file_path_out = os.path.join(results_dir, filename)

    with open(file_path_out, 'w', encoding='utf-8') as f:
        try:
            process = subprocess.Popen(
                ["pytest", file_path, "--tb=short", "--color=no"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            for line in process.stdout:
                f.write(line)
            process.wait()
        except subprocess.TimeoutExpired:
            f.write("Test execution timed out.\n")
        except Exception as e:
            f.write(f"Error running tests: {str(e)}\n")
    return file_path_out