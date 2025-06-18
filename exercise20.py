def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)

# Example:
print(count_vowels("This is a test sentence."))

