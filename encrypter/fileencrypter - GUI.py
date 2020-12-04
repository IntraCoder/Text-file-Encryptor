from tkinter import *
from tkinter import messagebox as msg
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from encrypter import fileencrypter_CLI

root = Tk()
root.geometry("440x300")
root.title("Encryptor")

# TODO-> Importing images (you may remove image part )
back = Image.open("background.jfif")
back = ImageTk.PhotoImage(back)
fold = PhotoImage(file="folder-icon.png")
key_img = PhotoImage(file="key_img.png")


# TODO -> Function to choose file to encrypt
def file_chooser():
    filename = askopenfilename()
    file_ent.delete(0, END)
    file_ent.insert(0, filename)


# TODO -> Function to open key
def key_chooser():
    keyname = askopenfilename()
    key_ent.delete(0, END)
    key_ent.insert(0, keyname)


# TODO -> Function to encrypt
def encrypt():
    if file_var.get() != "" and key_var.get() != "":  # Check if Entry box is not empty
        try:
            fileencrypter_CLI.crypt(file_var.get(), key_var.get(), "encrypt")
            msg.showinfo("Successful", f"Encryption of {file_var.get().split('/')[-1]} was successful")
        except ValueError:  # Proper Key file must be input
            msg.showerror("Error", "Fernet key must be 32 url-safe base64-encoded bytes.")
    else:  # Nothing happens for empty entry
        pass


# TODO -> Function to decrypt
def decrypt():
    if file_var.get() != "" and key_var.get() != "":  # Check if Entry box is not empty
        try:
            fileencrypter_CLI.crypt(file_var.get(), key_var.get(), "decrypt")
            msg.showinfo("Successful", f"Decryption of {file_var.get().split('/')[-1]} was successful")
        except ValueError:  # Proper Key file must be input
            msg.showerror("Error", "Fernet key must be 32 url-safe base64-encoded bytes.")
    else:  # Nothing happens for empty entry
        pass


Label(root, image=back).place(x=0, y=-50)

file_var = StringVar()
key_var = StringVar()

file_ent = Entry(root, textvariable=file_var, font=("Bahnschrift SemiBold Condensed", 17))
key_ent = Entry(root, textvariable=key_var, font=("Bahnschrift SemiBold Condensed", 17))

encrypt_but = Button(root, text="Encrypt", height=1, borderwidth=0, background="grey25", font="None 17",
                     foreground="white", command=encrypt, width=10)
decrypt_but = Button(root, text="Decrypt", height=1, borderwidth=0, background="grey25", font="None 17",
                     foreground="white", command=decrypt, width=10)
choose_file = Button(root, text="Choose File", image=fold, borderwidth=0, command=file_chooser)
choose_key = Button(root, text="Choose Key", image=key_img, borderwidth=0, command=key_chooser)

file_ent.place(x=125, y=100)
key_ent.place(x=125, y=170)
choose_file.place(x=80, y=100)
choose_key.place(x=80, y=170)
encrypt_but.place(x=100, y=240)
decrypt_but.place(x=250, y=240)

root.mainloop()
