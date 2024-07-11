import ast
import math
import resource
import subprocess
import time


# def bytes_to_human_readable(bytes_value):
#     kb_value = bytes_value / 1024
#     return f"{math.ceil(kb_value)} KB"

def run_python_code(python_code,function, timeout):
    try:
        with open('temp.py', 'w') as file:
            file.write(python_code)
            file.write(function)

        start_time = time.time()
        process = subprocess.Popen(['/var/www/codequest/venv/bin/python', 'temp.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        stdout, stderr = process.communicate(timeout=timeout)

        end_time = time.time()
        execution_time_ms = math.ceil((end_time - start_time) * 1000)

        max_rss_kb = math.ceil(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024)

        return stdout.strip(), execution_time_ms, max_rss_kb

    except subprocess.TimeoutExpired:
        raise TimeoutError("Execution time exceeded, action stopped.")


def get_actual_type(data_str):
    try:
        value = ast.literal_eval(data_str)
        actual_type = type(value).__name__
    except (ValueError, SyntaxError):
        value = str(data_str)
        actual_type = "invalid"
    return value, actual_type
