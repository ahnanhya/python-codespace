import numpy as num

random_array = num.random.rand(10)

mean = num.mean(random_array)
median = num.median(random_array)
std = num.std(random_array)

print(f"Random Array: {random_array}")
print(f"Mean:{mean}")
print(f"Median:{median}")
print(f"Standard Deviation: {std}")
