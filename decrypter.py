import os
import pyaes

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)
    
    original_file_path = file_path.replace(".ransoncript", "")
    with open(original_file_path, "wb") as new_file:
        new_file.write(decrypt_data)
    
    os.remove(file_path)
    print(f"Arquivo {file_path} descriptografado com sucesso!")

# Definir chave de descriptografia
key = b"cripto_bootcamp1"  # 16 bytes

# Buscar todos os arquivos .ransoncript no diretório atual
for file_name in os.listdir():
    if file_name.endswith(".ransoncript"):
        decrypt_file(file_name, key)
