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

text = "aaaa"
encrypted_text = encrypt(text, 2)
print(encrypted_text)

def brute_force(ciphertext, text):
    for i in range(26):
        decrypted_text = decrypt(ciphertext, i)
        if decrypted_text == text:
            print("Successfully cracked: ", decrypted_text)
            return
    print("Failed to crack the ciphertext")

brute_force(encrypted_text, text)