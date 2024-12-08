from collections import Counter

def char_frequency(s):
    return dict(Counter(s))

s=input("enter a string:")
print(char_frequency(s))