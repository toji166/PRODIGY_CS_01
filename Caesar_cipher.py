def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(message, shift):
    result = ""
    for char in message:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)   
        elif char.islower():
              result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

message = input("Enter your message: ")
shift = int(input("Enter shift value: ")) 

encrypted = encrypt(message,shift)
print("\n Encrypted Message: ", encrypted)

decrypted = decrypt(encrypted,shift)
print("\n Decrypted Message: ", decrypted)