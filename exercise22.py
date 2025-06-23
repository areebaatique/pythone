def simple_cipher(word):
    result = ""
    for char in word:
        if char.isalpha():
            # handle wrap around for 'z' and 'Z'
            if char == 'z':
                result += 'a'
            elif char == 'Z':
                result += 'A'
            else:
                result += chr(ord(char) + 1)
        else:
            result += char
    return result

# Example:
print(simple_cipher("abcZz"))
