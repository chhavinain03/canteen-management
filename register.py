import tkinter as tk
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="disha2003",
    database="collegedb"
)

# Create a cursor to execute SQL statements
cursor = db.cursor()

# Create a function to insert data into the table
def insert_data():
    
    username = username_entry.get()
    password = password_entry.get()
    contact = contact_entry.get()
    branch = branch_entry.get()
    
    # Execute the SQL statement to insert the data
    sql = "INSERT INTO studnt (username, password, contact, branch) VALUES ( %s, %s, %s, %s)"
    values = (username, password, contact, branch)
    cursor.execute(sql, values)
    db.commit()
    
    # Clear the entry fields
    
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)
    
    # Show a message to indicate the data was successfully inserted
    message_label.config(text="Data successfully inserted!")

# Create the Tkinter window
window = tk.Tk()
window.title("Insert data into SQL table")

# Create the entry fields for the user to input data


username_label = tk.Label(window, text="Username:")
username_label.grid(row=1, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(window)
password_entry.grid(row=2, column=1)

contact_label = tk.Label(window, text="Contact:")
contact_label.grid(row=3, column=0)
contact_entry = tk.Entry(window)
contact_entry.grid(row=3, column=1)

branch_label = tk.Label(window, text="Branch:")
branch_label.grid(row=4, column=0)
branch_entry = tk.Entry(window)
branch_entry.grid(row=4, column=1)

# Create a button to insert the data
insert_button = tk.Button(window, text="Insert data", command=insert_data)
insert_button.grid(row=5, column=0)

# Create a label to display messages
message_label = tk.Label(window, text="")
message_label.grid(row=6, column=0)

# Run the Tkinter main loop
window.mainloop()
