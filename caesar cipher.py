def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            else:
                result += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example usage:
text = "nama saya agung tirta yasha "
shift = 3
encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print(f"Original text: {text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")