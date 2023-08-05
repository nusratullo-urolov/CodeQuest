import ast
import math
import resource
import subprocess
import time


# def bytes_to_human_readable(bytes_value):
#     kb_value = bytes_value / 1024
#     return f"{math.ceil(kb_value)} KB"

def run_python_code(python_code, timeout):
    try:
        # Save the Python code to a temporary file
        with open('temp.py', 'w') as file:
            file.write(python_code)

        # Execute the Python program using python
        start_time = time.time()
        process = subprocess.Popen(['python', 'temp.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Wait for the subprocess to finish or raise TimeoutExpired
        stdout, stderr = process.communicate(timeout=timeout)

        # Calculate execution time in milliseconds and round it up
        end_time = time.time()
        execution_time_ms = math.ceil((end_time - start_time) * 1000)

        # Get memory usage of the subprocess and round it up to KB
        max_rss_kb = math.ceil(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024)

        # Return the output, execution time in milliseconds, and memory usage in KB
        return stdout.strip(), execution_time_ms, max_rss_kb

    except subprocess.TimeoutExpired:
        # If the subprocess takes longer than the specified timeout, handle the timeout here
        raise TimeoutError("Execution time exceeded, action stopped.")


def get_actual_type(data_str):
    try:
        value = ast.literal_eval(data_str)
        actual_type = type(value).__name__
    except (ValueError, SyntaxError):
        value = str(data_str)
        actual_type = "invalid"
    return value, actual_type
