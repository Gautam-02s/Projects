import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.title("Password Manager")

def add_password():
    website = simpledialog.askstring("Input", "Enter the website:")
    username = simpledialog.askstring("Input", "Enter your username:")
    password = simpledialog.askstring("Input", "Enter your password:")
    
    passwords[website] = {"username": username, "password": password}

def view_password():
    website = simpledialog.askstring("Input", "Enter the website:")
    
    if website in passwords:
        tk.messagebox.showinfo("Password", f"Username: {passwords[website]['username']}\nPassword: {passwords[website]['password']}")
    else:
        tk.messagebox.showinfo("Error", "Website not found in the password manager.")

def delete_password():
    website = simpledialog.askstring("Input", "Enter the website to delete:")
    
    if website in passwords:
        del passwords[website]
        tk.messagebox.showinfo("Success", f"{website} deleted from the password manager.")
    else:
        tk.messagebox.showinfo("Error", "Website not found in the password manager.")


add_button = tk.Button(root, text="Add Password", command=add_password)
view_button = tk.Button(root, text="View Password", command=view_password)
delete_button = tk.Button(root, text="Delete Password", command=delete_password)

add_button.pack()
view_button.pack()
delete_button.pack()

passwords = {}
root.mainloop()

