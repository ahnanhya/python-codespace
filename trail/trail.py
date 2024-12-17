from collections import Counter

def find_value_frequency(dictionary):
    # Using Counter to count the frequency of values in the dictionary
    value_frequency = Counter(dictionary.values())
    return value_frequency

# Example usage:
my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
value_frequency = find_value_frequency(my_dict)

# Displaying the frequency of each value
for value, count in value_frequency.items():
    print(f"Value {value}: {count} times")
