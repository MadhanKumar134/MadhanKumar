from tkinter import *

# Create the main window
root = Tk()

# Set the window title
root.title("Example Form")

# Set the window size
root.geometry("400x300")

# Create a label for the name field
name_label = Label(root, text="Name:")
name_label.pack()

# Create an entry field for the name
name_entry = Entry(root)
name_entry.pack()

# Create a label for the email field
email_label = Label(root, text="Email:")
email_label.pack()

# Create an entry field for the email
email_entry = Entry(root)
email_entry.pack()

# Create a button to submit the form
submit_button = Button(root, text="Submit")
submit_button.pack()

# Run the main loop
root.mainloop()
