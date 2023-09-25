import hashlib

def vigenere_decipher(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        key_char = key[i % key_length]
        decrypted_char = chr((ord(char) - ord(key_char)) % 256)
        decrypted_text += decrypted_char
        
    return decrypted_text

# Leer el mensaje cifrado y el hash del archivo mensajeseguro.txt
with open("mensajeseguro.txt", "r") as file:
    mensaje_cifrado = file.readline().strip()
    hash_original = file.readline().strip()

# Definir la misma clave utilizada para cifrar
clave = "clave"

# Descifrar el mensaje
mensaje_descifrado = vigenere_decipher(mensaje_cifrado, clave)

# Generar un hash del mensaje descifrado
hash_descifrado = hashlib.sha256(mensaje_descifrado.encode()).hexdigest()

# Verificar la integridad del mensaje
if hash_descifrado == hash_original:
    print("Mensaje no ha sido modificado. Mensaje original:")
    print(mensaje_descifrado)
else:
    print("El mensaje ha sido modificado. No se puede garantizar la integridad del mensaje.")
