def word_count(sentence):
    words = sentence.lower().split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

# Example:
print(word_count("This is a test. This test is simple."))

