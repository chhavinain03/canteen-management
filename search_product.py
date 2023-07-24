import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="disha2003",
  database="collegedb"
)


mycursor = mydb.cursor()

def update_product():
    
    product = product_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()
    
   
    sql = "UPDATE stocks SET price = %s, stock = %s WHERE product = %s"
    values = (price, stock, product)
    
    
    mycursor.execute(sql, values)
    
    
    mydb.commit()
    
   
    message_label.config(text="Product updated successfully!")

window = tk.Tk()
window.geometry=("800x900")
window["bg"]="black"


product_label = tk.Label(window, text="Product name:")
product_label.pack()
product_entry = tk.Entry(window)
product_entry.pack()

price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

stock_label = tk.Label(window, text="Stocks:")
stock_label.pack()
stock_entry = tk.Entry(window)
stock_entry.pack()


update_button = tk.Button(window, text="Update Product", command=update_product)
update_button.pack()


message_label = tk.Label(window, text="")
message_label.pack()

window.mainloop()
