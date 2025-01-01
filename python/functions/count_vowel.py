def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1
    return count

text=input("enter the string to check vowels:")
vowel_count=count_vowels(text)

print(f"The number of vowels in '{text}' is: {vowel_count}")
