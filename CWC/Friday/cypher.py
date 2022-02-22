def encrypt(text, key):
  result = ""

  for i in range(len(text)):
    char = text[i]

    if (char.isupper()):
      result += chr((ord(char) + key-65) % 26 + 65)
    elif char == '\n':
        result += char
    elif char.isdigit():
        result += str((int(char) + key) % 10)
    else:
      result += chr((ord(char) + key - 97) % 26 + 97)
  return result


def decrypt(text, key):
  result = ""

  for i in range(len(text)):
    char = text[i]

    if (char.isupper()):
      result += chr((ord(char) - key-65) % 26 + 65)
    elif char == '\n':
        result += char
    elif char.isdigit():
        result += str((int(char) - key) % 10)
    else:
      result += chr((ord(char) - key - 97) % 26 + 97)
  return result
