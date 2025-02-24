def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Execution of divide_numbers completed.")

# Test cases
print(divide_numbers(10, 2))  # Valid division
print(divide_numbers(10, 0))  # ZeroDivisionError
print(divide_numbers(10, 'a'))  # TypeError



