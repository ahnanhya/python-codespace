def exception_handling_demo():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

exception_handling_demo()


