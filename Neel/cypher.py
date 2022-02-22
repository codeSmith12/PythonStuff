def encrypt(text, key):
    encrypted = ""
    for c in text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else: # If its not alphabetical or a number, leave as is...
            encrypted += c
    return encrypted

def decrypt(text, key):
    decrypted = ""
    for c in text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index - key) % 26 + ord('A')
            c_new = chr(c_shifted)
            decrypted += c_new
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index - key) % 26 + ord('a')
            c_new = chr(c_shifted)
            decrypted += c_new
        elif c.isdigit():
            c_new = (int(c) - key) % 10
            decrypted += str(c_new)
        else: # If its not alphabetical or a number, leave as is...
            decrypted += c
    return decrypted
