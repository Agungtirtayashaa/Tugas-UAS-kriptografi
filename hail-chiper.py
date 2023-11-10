# Fungsi untuk mengenkripsi pesan menggunakan Hail Cipher
def encrypt(text):
    # Mengubah teks menjadi huruf kecil dan membersihkan dari spasi
    text = text.lower().replace(" ", "")
    encrypted_text = ""

    # Membuat list untuk menyimpan karakter pada posisi genap dan ganjil
    even_chars = []
    odd_chars = []

    # Memisahkan karakter pada posisi genap dan ganjil
    for i in range(len(text)):
        if i % 2 == 0:
            even_chars.append(text[i])
        else:
            odd_chars.append(text[i])

    # Menggabungkan karakter pada posisi genap dan ganjil
    encrypted_text = ''.join(odd_chars) + ''.join(even_chars)

    return encrypted_text

# Fungsi untuk mendekripsi pesan yang dienkripsi menggunakan Hail Cipher
def decrypt(text):
    decrypted_text = ""
    
    # Membagi teks menjadi dua bagian
    mid = len(text) // 2
    odd_chars = list(text[:mid])
    even_chars = list(text[mid:])

    # Menggabungkan kembali karakter yang telah dipisahkan
    for i in range(len(text)):
        if i % 2 == 0:
            decrypted_text += even_chars.pop(0)
        else:
            decrypted_text += odd_chars.pop(0)

    return decrypted_text

# Contoh penggunaan
pesan = "AGung sedang mengerjakan uts "
pesan_terenkripsi = encrypt(pesan)
pesan_terdekripsi = decrypt(pesan_terenkripsi)

print("Pesan Asli:", pesan)
print("Pesan Terenkripsi:", pesan_terenkripsi)
print("Pesan Terdekripsi:", pesan_terdekripsi)