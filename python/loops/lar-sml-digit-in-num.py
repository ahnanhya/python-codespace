 
def Digits(n): 
	largest = 0
	smallest = 9

	while (n): 
		r = n % 10

		# Find the largest digit 
		largest = max(r, largest) 

		# Find the smallest digit 
		smallest = min(r, smallest) 

		n = n // 10

	print(f"the largest is {largest}")
	print(f"the smallest is {smallest}")

n=int(input("enter a number :"))

Digits(n) 

