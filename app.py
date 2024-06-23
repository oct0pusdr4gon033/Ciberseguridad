import tkinter as tk
from tkinter import messagebox

def xor_encrypt_decrypt(message, key):
    message_chars = list(message)
    key_chars = list(key)
    extended_key = key_chars * (len(message) // len(key_chars)) + key_chars[:len(message) % len(key_chars)]
    result_chars = [chr(ord(m) ^ ord(k)) for m, k in zip(message_chars, extended_key)]
    result = ''.join(result_chars)
    return result

def encrypt_message():
    global last_key
    message = message_entry.get()
    key = key_entry.get()
    if not message or not key:
        messagebox.showerror("Error", "El mensaje y la clave no pueden estar vacíos.")
        return
    encrypted_message = xor_encrypt_decrypt(message, key)
    result_text.set(encrypted_message)
    last_key = key
    message_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)

def decrypt_message():
    global last_key
    encrypted_message = message_entry.get()
    key = key_entry.get()
    if not encrypted_message or not key:
        messagebox.showerror("Error", "El mensaje encriptado y la clave no pueden estar vacíos.")
        return
    if key != last_key:
        messagebox.showerror("Error", "La clave ha cambiado. No se puede desencriptar.")
        return
    decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
    result_text.set(decrypted_message)
    message_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)

def toggle_visibility():
    current_state = key_entry.cget("show")
    if current_state == "":
        key_entry.config(show="*")
    else:
        key_entry.config(show="")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Encriptación")

# Variable global para almacenar la última clave utilizada para encriptar
last_key = None

# Campos de entrada para el mensaje y la clave
tk.Label(root, text="Mensaje:").grid(row=0, column=0, padx=10, pady=10)
message_entry = tk.Entry(root, width=50)
message_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Clave:").grid(row=1, column=0, padx=10, pady=10)
key_entry = tk.Entry(root, width=50, show="*")
key_entry.grid(row=1, column=1, padx=10, pady=10)

# Botones para encriptar y desencriptar
encrypt_button = tk.Button(root, text="Encriptar", command=encrypt_message)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Desencriptar", command=decrypt_message)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Botón para alternar visibilidad de la clave
toggle_button = tk.Button(root, text="Mostrar Clave", command=toggle_visibility)
toggle_button.grid(row=1, column=2, padx=10, pady=10)

# Campo para mostrar el resultado
result_text = tk.StringVar()
tk.Label(root, text="Resultado:").grid(row=3, column=0, padx=10, pady=10)
result_label = tk.Entry(root, textvariable=result_text, width=50)
result_label.grid(row=3, column=1, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
