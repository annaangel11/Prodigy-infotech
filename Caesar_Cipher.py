import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha(): 
            shift_amount = shift % 26 
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift_amount) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift_amount) % 26 + 97)
        else:
            encrypted_text += char  
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)


def process_cipher():
    message = entry_message.get()
    shift = entry_shift.get()

   
    if not shift.isdigit():
        messagebox.showerror("Invalid Input", "Shift value must be a number!")
        return

    shift = int(shift)
    if var.get() == 1:  
        result = encrypt(message, shift)
    elif var.get() == 2: 
        result = decrypt(message, shift)
    else:
        result = "Please select Encrypt or Decrypt"

    entry_result.delete(0, tk.END) 
    entry_result.insert(0, result) 


root = tk.Tk()
root.title("Caesar Cipher")

label_message = tk.Label(root, text="Enter your message:")
label_message.grid(row=0, column=0, padx=10, pady=10)

entry_message = tk.Entry(root, width=40)
entry_message.grid(row=0, column=1, padx=10, pady=10)

label_shift = tk.Label(root, text="Enter the shift value:")
label_shift.grid(row=1, column=0, padx=10, pady=10)

entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=1, column=1, padx=10, pady=10)

var = tk.IntVar()
var.set(1) 

radio_encrypt = tk.Radiobutton(root, text="Encrypt", variable=var, value=1)
radio_encrypt.grid(row=2, column=0, padx=10, pady=10)

radio_decrypt = tk.Radiobutton(root, text="Decrypt", variable=var, value=2)
radio_decrypt.grid(row=2, column=1, padx=10, pady=10)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=3, column=0, padx=10, pady=10)

entry_result = tk.Entry(root, width=40)
entry_result.grid(row=3, column=1, padx=10, pady=10)

button_process = tk.Button(root, text="Process", command=process_cipher)
button_process.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

