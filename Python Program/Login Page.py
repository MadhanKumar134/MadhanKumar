import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == 'Madhan' and password == '6379468445':
        message_label.config(text='Login successful!', fg='green')
    else:
        message_label.config(text='Invalid username or password', fg='red')

# Set up the window
window = tk.Tk()
window.title('Login Page')
window.geometry('300x200')

# Set up the widgets
username_label = tk.Label(window, text='Username:')
username_entry = tk.Entry(window)
password_label = tk.Label(window, text='Password:')
password_entry = tk.Entry(window, show='*')
login_button = tk.Button(window, text='Login', command=login)
message_label = tk.Label(window, text='')

# Add the widgets to the window
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()
message_label.pack()

# Set the background color
window.configure(bg='#FFA500')

# Start the event loop
window.mainloop()
