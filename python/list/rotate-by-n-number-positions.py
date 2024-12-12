def rotate_list(lst, n):
    n = n % len(lst)  # Handle cases where N is larger than the list length
    return lst[-n:] + lst[:-n]

# Example usage:
lst = [1, 2, 3, 4, 5]
n = 2
print(rotate_list(lst, n))  # Output: [4, 5, 1, 2, 3]
