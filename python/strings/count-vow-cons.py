vowels="aeiouAEIOU"

vowels_count=0
consonant_count=0

string=input("enter a string:")

for char in string:
    if char.isalpha():
        if char in vowels :
            vowels_count+=1
        else:
            consonant_count+=1

print(f"the number of vowels is {vowels_count}")
print(f"the number of consonants is {consonant_count}")