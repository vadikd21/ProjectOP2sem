#Функція для шифрування тексту шифром Цезаря:
def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text
#Функція для дешифрування тексту способом Цезаря:
def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text
#Функція для шифрування тексту способом Віженера
def encrypt_vigenere(plaintext, keyword):
    encrypted_text = ""
    keyword_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[keyword_index].upper())- ord('A')
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            encrypted_text += char
    return encrypted_text
