from cryptography.fernet import Fernet

# This code generates a key for encryption and saves it in a file for later use
# Never Lose your key as it is the key to decrypt your encrypted data
# Keep this key safe
key = Fernet.generate_key()
key_file = open("key_store.key", "wb")
key_file.write(key)
key_file.close()
