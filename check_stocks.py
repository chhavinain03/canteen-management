import mysql.connector
from tkinter import *

# Function to check stock level
def check_stock():
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="disha2003",
        database="collegedb"
    )
    
    # Get the stock level of the product
    mycursor = mydb.cursor()
    mycursor.execute("SELECT stock FROM stocks WHERE product=%s", (product_name.get(),))
    result = mycursor.fetchone()
    current_stock = result[0]
    
    # Check if the new stock level is within the limit
    new_stock = int(product_stock.get())
    if (current_stock + new_stock) < 40:
        error_label.config(text="Error: Stock level cannot go below 40.")
    else:
        error_label.config(text="")
        
        # Update the stock level in the database
        mycursor.execute("UPDATE stocks SET stock=%s WHERE product=%s", (new_stock, product_name.get()))
        mydb.commit()
        success_label.config(text="Stock level updated successfully.")

# Create the GUI
root = Tk()
root.title("Stock Manager")

# Create the input fields
product_name_label = Label(root, text="Product Name:")
product_name_label.grid(row=0, column=0)
product_name = Entry(root)
product_name.grid(row=0, column=1)

product_price_label = Label(root, text="Product Price:")
product_price_label.grid(row=1, column=0)
product_price = Entry(root)
product_price.grid(row=1, column=1)

product_stock_label = Label(root, text="Product Stock:")
product_stock_label.grid(row=2, column=0)
product_stock = Entry(root)
product_stock.grid(row=2, column=1)

# Create the error and success labels
error_label = Label(root, fg="red")
error_label.grid(row=3, column=1)

success_label = Label(root, fg="green")
success_label.grid(row=4, column=1)

# Create the update button
update_button = Button(root, text="Update Stock", command=check_stock)
update_button.grid(row=3, column=0)

root.mainloop()
