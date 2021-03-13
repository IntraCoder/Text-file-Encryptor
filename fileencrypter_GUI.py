from tkinter import *
from tkinter import messagebox as msg
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from cryptography.fernet import Fernet, InvalidToken

root = Tk()
root.geometry("410x340")
root.title("Encryptor")

# TODO-> Importing images (you may remove image part )
back = Image.open("background.jfif")
back = ImageTk.PhotoImage(back)
fold = PhotoImage(file="folder-icon.png")
key_img = PhotoImage(file="key_img.png")


# TODO -> Function to choose file to encrypt
def file_chooser():
    filename = askopenfilename()
    file_var.set(filename)


# TODO -> Function to open key
def key_chooser():
    keyname = askopenfilename()

    key_var.set(keyname)


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
    log_lb.config(text="[+] Fetching key...")
    key = Fernet(key)
    text = file_work(file_name, "rb")
    log_lb.config(text="[+] Reading File...")

    if cryption == "encrypt":
        try:
            log_lb.config(text="[+] Encrypting Data...")
            for i in range(num):
                text = key.encrypt(text)
            log_lb.config(text="[+] Encryption Successful!")
            file_work(file_name, "wb", text, True)
        except UnicodeDecodeError:
            log_lb.config(text="[-] Type Error : Cannot encrypt files of this type.")
        except MemoryError:
            log_lb.config(text="EOF Error : Encrypted text out of limit.")

    elif cryption == "decrypt":
        try:
            log_lb.config(text="[+] Decrypting Data...")
            for i in range(num):
                text = key.decrypt(text)
            file_work(file_name, "wb", text, True)
            log_lb.config(text="[+] Decryption Successful!")
        except InvalidToken:
            log_lb.config(text="[+] Already Decrypted!")


# TODO -> Function to encrypt
def encrypt():
    if file_var.get() != "" and key_var.get() != "":  # Check if Entry box is not empty
        try:
            crypt(file_var.get(), key_var.get(), "encrypt", time_var.get())
        except ValueError:  # Proper Key file must be input
            log_lb.config(text="[-] Error : Fernet key must be 32 url-safe base64-encoded bytes.")

    else:  # Nothing happens for empty entry
        pass


# TODO -> Function to decrypt
def decrypt():
    if file_var.get() != "" and key_var.get() != "":  # Check if Entry box is not empty

        crypt(file_var.get(), key_var.get(), "decrypt", time_var.get())
        print(file_work(file_var.get(), "rb").decode())
    else:  # Nothing happens for empty entry
        pass


Label(root, image=back).place(x=0, y=-50)
Label(root, text="Times", font=("Bahnschrift SemiBold Condensed", 17)).place(x=50, y=180)

file_var = StringVar()
key_var = StringVar()
time_var = IntVar()
time_var.set(1)

Entry(root, textvariable=file_var, font=("Bahnschrift SemiBold Condensed", 17), relief=SUNKEN, bd=3,
      width=23).place(x=125, y=80)
Entry(root, textvariable=key_var, font=("Bahnschrift SemiBold Condensed", 17), relief=SUNKEN, bd=3,
      width=23).place(x=125, y=130)
Entry(root, textvariable=time_var, font=("Bahnschrift SemiBold Condensed", 17), relief=SUNKEN, bd=3,
      width=23).place(x=125, y=180)

Button(root, text="Encrypt", height=1, borderwidth=0, background="grey25", font="None 17",
       foreground="white", command=encrypt, width=10, relief=RAISED).place(x=80, y=240)
Button(root, text="Decrypt", height=1, borderwidth=0, background="grey25", font="None 17",
       foreground="white", command=decrypt, width=10, relief=RAISED).place(x=230, y=240)

Button(root, text="Choose File", image=fold, command=file_chooser, relief=RAISED).place(x=60, y=80)

Button(root, text="Choose Key", image=key_img, command=key_chooser, relief=RAISED).place(x=60, y=130)

log_lb = Label(root, relief=RAISED, font=("Bahnschrift SemiBold Condensed", 15), justify=LEFT, bd=4, width=54)
log_lb.pack(side=BOTTOM)

root.mainloop()
