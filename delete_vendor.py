import tkinter as tk
import mysql.connector

# Create a connection to the database
conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="Pyadav@29",
       database="vendor"
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a function to execute the delete query and display the results
def delete_students():
    # Get the value of the vendor name field
    students_name = name_entry.get()

    # Execute the SQL query with the vendor name
    cursor.execute("DELETE FROM vendors WHERE name=?", (students_name,))
    conn.commit()

    # Clear the vendor name field
    name_entry.delete(0, tk.END)

# Display a message indicating the vendor has been deleted
    message_label.config(text=f"{vendor_name} has been deleted from the database.")

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Delete Vendor")

# Create a vendor name label and entry field
name_label = tk.Label(window, text="Vendor Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Create a delete button
delete_button = tk.Button(window, text="Delete", command=delete_students)
delete_button.pack()

# Create a message label to display the result of the delete operation
message_label = tk.Label(window, text="VENDOR DELETED SUCCESSFULLY!")
message_label.pack()

# Run the main window loop
window.mainloop()
