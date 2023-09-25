import hashlib

def vigenere_cipher(texto, key):
    cifrado = ""
    key_len = len(key)
    
    for i in range(len(texto)):
        char = texto[i]
        key_char = key[i % key_len]
        cifrado_char = chr((ord(char) + ord(key_char)) % 256)
        cifrado += cifrado_char
        
    return cifrado

# Leer el mensaje de entrada
with open("mensajedeentrada.txt", "r") as file:
    mensaje_original = file.read()

# Definir una clave para el cifrado Vigenère
clave = "clave"

# Cifrar el mensaje
mensaje_cifrado = vigenere_cipher(mensaje_original, clave)

# Generar un hash del mensaje original
hash_original = hashlib.sha256(mensaje_original.encode()).hexdigest()

# Escribir el mensaje cifrado y el hash en el archivo mensajeseguro.txt
with open("mensajeseguro.txt", "w") as file:
    file.write(mensaje_cifrado + "\n")
    file.write(hash_original)
