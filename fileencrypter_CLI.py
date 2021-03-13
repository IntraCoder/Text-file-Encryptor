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

def crypt(file_name, key_file, cryption, num):
    key = file_work(key_file, "rb")
    print("[+] Fetching key...")
    key = Fernet(key)
    text = file_work(file_name, "rb")
    print("[+] Reading File...")

    if cryption == "encrypt":
        try:
            print("[+] Encrypting Data...")
            for i in range(num):
                text = key.encrypt(text)
            print("[+] Encryption Successful!")
            file_work(file_name, "wb", text, True)
        except UnicodeDecodeError:
            print("[-] Type Error : Cannot encrypt files of this type. ")
            msg.showerror("Error", "Cannot encrypt files of this type.")
        except MemoryError:
            print("[-] EOF Error : Encrypted text out of limit.")
            msg.showerror("EOF error", "Encrypted text out of limit.")

    elif cryption == "decrypt":
        try:
            print("[+] Decrypting Data...")
            for i in range(num):
                text = key.decrypt(text)
            file_work(file_name, "wb", text, True)
            print("[+] Decryption Successful!")
        except:
            print("[+] Already Decrypted!")


if __name__ == '__main__':  # You can remove this condition if only using command line encrypter
    key = input("Enter Key file name:")
    file = input("Enter file name to encrypt/decrypt:")
    cryption = input("Encrypt or Decrypt: ")
    num = int(input("Enter number of times:"))
    if cryption.lower() == "encrypt":
        crypt(file, key, "encrypt", num)
    elif cryption.lower() == "decrypt":
        crypt(file, key, "decrypt", num)
    else:
        print("[-] Please enter a valid input!")
