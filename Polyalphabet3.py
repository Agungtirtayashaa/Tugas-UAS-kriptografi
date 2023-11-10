def polialphabet_cipher(text, key1, key2, key3, mode):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    
    for char in text:
        if char.isalpha():
            if char.islower():
                alphabet = alphabet.lower()
            index = alphabet.index(char.upper())
            if mode == 'encrypt':
                result += alphabet[(index + key1) % 26]
                alphabet = alphabet[::-1]
                result += alphabet[(index + key2) % 26]
                alphabet = alphabet[::-1]
                result += alphabet[(index + key3) % 26]
                alphabet = alphabet[::-1]
            elif mode == 'decrypt':
                result += alphabet[(index - key1) % 26]
                alphabet = alphabet[::-1]
                result += alphabet[(index - key2) % 26]
                alphabet = alphabet[::-1]
                result += alphabet[(index - key3) % 26]
                alphabet = alphabet[::-1]
        else:
            result += char
    
    return result

# Contoh penggunaan untuk mengenkripsi teks
plaintext = "TULIS TEKS INI"
key1 = 3
key2 = 5
key3 = 7
encrypted_text = polialphabet_cipher(plaintext, key1, key2, key3, 'encrypt')
print("Teks Terenkripsi:", encrypted_text)

# Contoh penggunaan untuk mendekripsi teks
decrypted_text = polialphabet_cipher(encrypted_text, key1, key2, key3, 'decrypt')
print("Teks Terdekripsi:", decrypted_text)
