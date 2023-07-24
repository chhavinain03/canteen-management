import tkinter as tk
import mysql.connector



db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="disha2003",
    database="collegedb"
)
def delete():
    product = product_entry.get()
    price = price_entry.get()


    cursor = db.cursor()
    sql =  "DELETE FROM STOCKS WHERE product=%s AND price=%s"
    values = (product,price)
    cursor.execute(sql,values)
    db.commit()
    message_label.config(text="Data successfully deleted!")


root = tk.Tk()
root.title("DELETE PAGE")
root["bg"]="black"
root.geometry("400x150")


product_label = tk.Label(root, text="product")
product_label.pack()
product_entry = tk.Entry(root)
product_entry.pack()

price_label = tk.Label(root, text="Price")
price_label.pack()
price_entry = tk.Entry(root, show="*")
price_entry.pack()


login_button = tk.Button(root, text="Delete", command=delete)
login_button.pack()
message_label = tk.Label(root, text="")
message_label.pack()



root.mainloop()
