import tkinter
import customtkinter
import random
import os
from cryptography.fernet import Fernet

# Initializing Tkinter Window
app = customtkinter.CTk()
app.title("Password Generator")
width = 800
height = 600
app.geometry(f'{width}x{height}')
bg = customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


# Password Generator, Maps to label
def PwrdGenerator():
    Char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&"
    shuffled = ''.join(random.sample(Char,len(Char)))
    p_length = int(slider.get())
    global password
    password = ''
    for i in range(p_length):
        password += random.choice(shuffled)
    return display_pward.configure(text=password)


# Save function
def save():
    if not len(pwrd_name.get()) == 0:
        decrypt()
        with open("test.txt", 'a') as txt:
            txt.write(f'{pwrd_name.get()}: {password}\n')
        encrypt()
        pwrd_name.delete(0, 'end')
        display_pward.pack_forget()
        display_pward.configure(text='Passwords')
    else:
        open_popup()

# Encryption function
def encrypt():
    files = []
    for file in os.listdir():
        if file == "tkntTest1.py" or file == "thekey.key":
            continue
        if os.path.isfile(file):
            files.append(file)
    key = Fernet.generate_key()
    with open("thekey.key", 'wb') as thekey:
        thekey.write(key)
    for file in files:
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, 'wb') as thefile:
            thefile.write(contents_encrypted)
    return
# Decryption function
def decrypt():
    files = []
    for file in os.listdir():
        if file == "tkntTest1.py" or file == "thekey.key":
            continue
        if os.path.isfile(file):
            files.append(file)

    with open("thekey.key", "rb") as key:
        secreykey = key.read()

    for file in files:
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secreykey).decrypt(contents)
        with open(file, 'wb') as thefile:
            thefile.write(contents_decrypted)
    return

# Password name label
def open_popup():
    top = customtkinter.CTkToplevel(app)
    top.geometry("400x300")
    top.title("Error")
    customtkinter.CTkLabel(top, text="Please Ender A Password Name", text_font=('Courier', 12, 'bold'),
                           fg_color='Red').place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    top.grab_set()

# Log in
def login_password():
    log_in_password = 'Test'
    if login_pwrd_name.get() == log_in_password:
        return login_frame.destroy()
    else:
        display_enter_password.configure(text="Wrong Password!")

# Saved passwords window
def saved_passwords():
    user_frame.destroy()
    decrypt()
    passwords = tkinter.Text(password_frame,width= width,height=height)
    filename = 'C:\\Users\\Stefano\\Documents\\GitHub\\Password-Generator\\tkinterTest\\test.txt'
    with open(filename, 'r') as f:
        passwords.insert('1.0', f.read())
    passwords.pack()
    encrypt()

# Log in frame
login_frame = customtkinter.CTkFrame(app,bg_color=bg,width=width,height=height)
login_frame.pack()

display_enter_password = customtkinter.CTkLabel(login_frame, text='Enter Password', corner_radius=8, fg_color="gray75",
                                                text_color='black', text_font=('Courier', 12, 'bold')
                                                )
display_enter_password.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER, width=350)

login_pwrd_name = customtkinter.CTkEntry(login_frame,show = "*")
login_pwrd_name.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

login_button = customtkinter.CTkButton(login_frame, text="Enter", command=login_password)
login_button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

# User frame
user_frame = customtkinter.CTkFrame(app, bg_color=bg, width=width, height=height)
user_frame.pack()

# Password display label
display_pward = customtkinter.CTkLabel(user_frame, text="Passwords", corner_radius=8, fg_color="gray75",
                                       text_color='black', text_font=('Courier', 12, 'bold')
                                       )
display_pward.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER, width=350)


# generate password button, mapped to PwrdGenerator
generate_bttn = customtkinter.CTkButton(user_frame, text="Generate", command=PwrdGenerator)
generate_bttn.place(relx=0.25, rely=0.25, anchor=tkinter.CENTER)

# Save button
save_bttn= customtkinter.CTkButton(user_frame, text="Save", command=save)
save_bttn.place(relx=0.75, rely=0.25, anchor=tkinter.CENTER)

# Name entry
pwrd_name = customtkinter.CTkEntry(user_frame)
pwrd_name.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

# Entry label
entry_label= customtkinter.CTkLabel(user_frame, text="Enter Password Name")
entry_label.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

# Slide bar
slider = customtkinter.CTkSlider(user_frame, from_=8, to=18)
slider.place(relx=0.75, rely=0.75, anchor=tkinter.CENTER)

# Slide bar label
slider_label = customtkinter.CTkLabel(user_frame,text="8 9 10 11 12 13 14 15 16 17 18", corner_radius=8,
                                      text_font=('Courier', 8, 'bold'))
slider_label.place(relx=0.75, rely=0.8, anchor=tkinter.CENTER)

# open saved passwords button
open_bttn = customtkinter.CTkButton(user_frame,text = "Saved Passwords",command = saved_passwords)
open_bttn.place(relx=0.25, rely=0.75, anchor=tkinter.CENTER)

# Saved passwords frame
password_frame = customtkinter.CTkFrame(app, bg_color=bg, width=width, height=height)
password_frame.pack()

app.mainloop()












