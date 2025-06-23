def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# Example:
print(reverse_words("Hello world this is fun"))


