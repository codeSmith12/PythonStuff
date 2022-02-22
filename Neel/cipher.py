def encrypt(text, offset):
    result = ""
    # Traverse the plain text
    for char in text:
        if (char.isupper()):
            result += chr((ord(char) + offset - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + offset - 97) % 26 + 97)
        elif char.isdigit():
            c_new = (int(char) + offset) % 10
            result += str(c_new)
        else:
            result += char
    return result

def decrypt(text, offset):
    result = ""
    # Traverse the plain text
    for char in text:
        if (char.isupper()):
            result += chr((ord(char) - offset - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - offset - 97) % 26 + 97)
        elif char.isdigit():
            c_new = (int(char) - offset) % 10
            result += str(c_new)
        else:
            result += char
    return result
