import tkinter as tk
import mysql.connector

# Establish a connection to the SQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="disha2003",
    database="collegedb"
)

# Define a function to verify the login credentials
def verify_login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()
    
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    
    # Execute a SELECT query to find a matching row in the studnt table
    query = "SELECT * FROM studnt WHERE username=%s AND password=%s"
    values = (username, password)
    cursor.execute(query, values)
    
    # Fetch the result of the query
    result = cursor.fetchone()
    
    # If a matching row was found, show the success label and hide the register label
    if result:
        success_label.config(text="Login successful!")
        register_label.pack_forget()
        success_label.pack()
    # Otherwise, show the register label and hide the success label
    else:
        register_label.config(text="Register first!")
        success_label.pack_forget()
        register_label.pack()

# Create the Tkinter window
root = tk.Tk()
root.title("Login Page")
root["bg"]="black"
root.geometry("400x150")

# Create the username label and entry widget
username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create the password label and entry widget
password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create the login button
login_button = tk.Button(root, text="Login", command=verify_login)
login_button.pack()

# Create the success label and hide it by default
success_label = tk.Label(root, text="")
success_label.pack()
success_label.config(fg="green", font=("Arial", 12))
success_label.pack_forget()

# Create the register label and hide it by default
register_label = tk.Label(root, text="")
register_label.pack()
register_label.config(fg="red", font=("Arial", 12))
register_label.pack_forget()

# Run the main loop of the window
root.mainloop()
