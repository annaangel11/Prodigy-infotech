import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os

# Function to encrypt an image
def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    
    pixels = np.array(image)
    width, height = image.size

    # Normalize the key to ensure it stays within 0-255
    key = key % 256

    # Encrypt each pixel with the key
    for i in range(height):
        for j in range(width):
            r, g, b = pixels[i, j]
            # Apply encryption (add key and ensure value stays within 0-255)
            pixels[i, j] = [(r + key) % 256, (g + key) % 256, (b + key) % 256]
    
    encrypted_image = Image.fromarray(pixels.astype('uint8'))
    encrypted_image.save(output_path)

# Function to decrypt an image
def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    
    pixels = np.array(image)
    width, height = image.size

    # Normalize the key to ensure it stays within 0-255
    key = key % 256

    # Decrypt each pixel with the key
    for i in range(height):
        for j in range(width):
            r, g, b = pixels[i, j]
            # Apply decryption (subtract key and ensure value stays within 0-255)
            pixels[i, j] = [(r - key) % 256, (g - key) % 256, (b - key) % 256]
    
    decrypted_image = Image.fromarray(pixels.astype('uint8'))
    decrypted_image.save(output_path)

# GUI application
class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor")
        self.root.geometry("400x400")

        # Image path
        self.image_path = None
        
        # Create widgets
        self.label = tk.Label(root, text="Select an Image to Encrypt/Decrypt")
        self.label.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=10)

        self.key_label = tk.Label(root, text="Enter Key (number)")
        self.key_label.pack(pady=10)

        self.key_entry = tk.Entry(root)
        self.key_entry.pack(pady=10)

        self.encrypt_button = tk.Button(root, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack(pady=5)

    # Select image file
    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            img = Image.open(self.image_path)
            img.thumbnail((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk

    # Encrypt image
    def encrypt_image(self):
        if self.image_path and self.key_entry.get().isdigit():
            key = int(self.key_entry.get())
            output_path = os.path.splitext(self.image_path)[0] + "_encrypted.jpg"
            encrypt_image(self.image_path, key, output_path)
            messagebox.showinfo("Success", f"Image encrypted and saved as {output_path}")
        else:
            messagebox.showerror("Error", "Please select an image and enter a valid key.")

    # Decrypt image
    def decrypt_image(self):
        if self.image_path and self.key_entry.get().isdigit():
            key = int(self.key_entry.get())
            output_path = os.path.splitext(self.image_path)[0] + "_decrypted.jpg"
            decrypt_image(self.image_path, key, output_path)
            messagebox.showinfo("Success", f"Image decrypted and saved as {output_path}")
        else:
            messagebox.showerror("Error", "Please select an image and enter a valid key.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()

