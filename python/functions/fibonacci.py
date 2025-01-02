def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms= int(input("enter a number:"))
for i in range(terms):
    print(f"Fibonacci term {i} is {fibonacci(i)}")
