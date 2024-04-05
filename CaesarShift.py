def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

print(encrypt("zzzz", 2))