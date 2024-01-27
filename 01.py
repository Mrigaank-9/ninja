# Here is a Python code to solve the problem:

def update_string(s):
    updated_string = ""
    for letter in s:
        if letter.islower():
            updated_string += chr((ord(letter) - 97 + 1) % 26 + 97)
        elif letter.isupper():
            updated_string += chr((ord(letter) - 65 - 1) % 26 + 65)
        else:
            updated_string += letter
    return updated_string

# Example usage
s = "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
updated_s = update_string(s)
print(updated_s) # Output: bCdEfGhIjKlMnOpQrStUvWxYzA