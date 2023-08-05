def execute_code(code_input):
    try:
        # Using eval to execute the Python code (Unsafe in production!)
        output = eval(code_input)
        return str(output)
    except Exception as e:
        return str(e)
