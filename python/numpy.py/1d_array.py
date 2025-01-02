import numpy as num

random_array = num.random.rand(10)

mean = num.mean(random_array)
median = num.median(random_array)
std = num.std(random_array)

print("Random Array:", random_array)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)
