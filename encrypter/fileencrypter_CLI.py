from cryptography.fernet import Fernet
from tkinter import messagebox as msg


# Before
# TODO -> Function to open file with required purpose(read->r,read byte->rb, write->w,write byte->wb etc)
# truncate -> Clear all content of the file,data -> data to write
def file_work(file_name, purpose, data=None, truncate=False):
    file = open(file_name, purpose)

    if "r" in purpose:
        content = file.read()
        file.close()
        return content

    elif "w" in purpose:
        if truncate:
            file.truncate()
        file.write(data)
    file.close()


# TODO -> Function for Encryption and Decryption

def crypt(file_name, key_file, cryption):
    key = file_work(key_file, "rb")
    print("[+] Fetching key...")
    key = Fernet(key)
    text = file_work(file_name, "r")
    print("[+] Reading File...")

    if cryption == "encrypt":
        try:
            print("[+] Encrypting Data...")
            text = key.encrypt(text.encode())
            print("[+] Encryption Successful")
            file_work(file_name, "wb", text, True)
        except UnicodeDecodeError:
            msg.showerror("Error", "Cannot encrypt files of this type.")

    elif cryption == "decrypt":
        try:
            print("[+] Decrypting Data...")
            text = key.decrypt(text.encode())
            file_work(file_name, "wb", text, True)
            print("[+] Decryption Successful")
        except:
            msg.showerror("Error", "The file is already encrypted")


if __name__ == '__main__':  # You can remove this condition if only using command line encrypter
    key = input("Enter Key file name:")
    file = input("Enter file name to encrypt/decrypt:")
    cryption = input("Encrypt or Decrypt: ")
    if cryption.lower() == "encrypt":
        crypt(file, key, "encrypt")
    elif cryption.lower() == "decrypt":
        crypt(file, key, "decrypt")
    else:
        print("Please enter a valid input!")
