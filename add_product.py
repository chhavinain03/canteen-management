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
    
    product = product_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()
  
    
    # Execute the SQL statement to insert the data
    sql = "INSERT INTO stocks (product, price, stock) VALUES ( %s, %s, %s)"
    values = (product, price, stock)
    cursor.execute(sql, values)
    db.commit()
    
    # Clear the entry fields
    
    product_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)
   
    
    # Show a message to indicate the data was successfully inserted
    message_label.config(text="Data successfully inserted!")

# Create the Tkinter window
window = tk.Tk()
window.title("Insert data into SQL table")

# Create the entry fields for the user to input data


product_label = tk.Label(window, text="Product")
product_label.grid(row=1, column=0)
product_entry = tk.Entry(window)
product_entry.grid(row=1, column=1)

price_label = tk.Label(window, text="Price")
price_label.grid(row=2, column=0)
price_entry = tk.Entry(window)
price_entry.grid(row=2, column=1)

stock_label = tk.Label(window, text="Stock:")
stock_label.grid(row=3, column=0)
stock_entry = tk.Entry(window)
stock_entry.grid(row=3, column=1)



# Create a button to insert the data
insert_button = tk.Button(window, text="Insert data", command=insert_data)
insert_button.grid(row=5, column=0)

# Create a label to display messages
message_label = tk.Label(window, text="")
message_label.grid(row=6, column=0)

# Run the Tkinter main loop
window.mainloop()
