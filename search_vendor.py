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

# Create a function to execute the search query and display the results
def search_students():
    # Get the value of the search field
    search_text = search_entry.get()

    # Execute the SQL query with the search text
    cursor.execute("SELECT * FROM vendors WHERE name LIKE ?", ('%' + search_text + '%',))
    results = cursor.fetchall()

    # Clear the results listbox
    results_listbox.delete(0, tk.END)
    
  # Loop through the results and add them to the listbox
    for students in results:
        results_listbox.insert(tk.END, students[1])

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Vendor Search")

# Create a search label and entry field
search_label = tk.Label(window, text="Search for Vendor:")
search_label.pack()
search_entry = tk.Entry(window)
search_entry.pack()

# Create a search button
search_button = tk.Button(window, text="Search", command=search_students)
search_button.pack()

# Create a listbox to display the search results
results_listbox = tk.Listbox(window)
results_listbox.pack()

# Run the main window loop
window.mainloop()
