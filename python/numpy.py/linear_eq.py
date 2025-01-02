import numpy as eq

A = eq.array([[2, 3], [1, 4]])

b = eq.array([5, 6])

#linalg function 
x = eq.linalg.solve(A, b)

print("Solution to the system of equations:", x)
