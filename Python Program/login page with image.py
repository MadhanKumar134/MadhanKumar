from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Login Page")

o# Load background image
bg_image = Image.open ("C:\Users\madha\Pictures\Wallpapes\3.jpg")
resized_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(resized_image)

# Create background label
bg_label = Label(root, image=tk_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create login form elements
username_label = Label(root, text="Username:")
username_entry = Entry(root)
password_label = Label(root, text="Password:")
password_entry = Entry(root, show="*")
login_button = Button(root, text="Login")

# Place login form elements on background label
username_label.place(relx=0.5, rely=0.35, anchor=CENTER)
username_entry.place(relx=0.5, rely=0.4, anchor=CENTER)
password_label.place(relx=0.5, rely=0.45, anchor=CENTER)
password_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
login_button.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
