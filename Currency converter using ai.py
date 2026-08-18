import tkinter as tk
from tkinter import ttk
import requests

def convert_currency():
    amount = float(amount_entry.get())
    target = target_currency.get()
    
    # Fetch live conversion rate
    url = f"https://open.er-api.com/v6/latest/INR"
    response = requests.get(url).json()
    rate = response['rates'][target]
    
    result = amount * rate
    result_label.config(text=f"{amount} INR = {result:.2f} {target}")

# Set up main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x200")

# Input widgets
tk.Label(root, text="Amount in INR:").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

tk.Label(root, text="Select Target Currency:").pack(pady=5)
target_currency = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY"])
target_currency.set("USD")
target_currency.pack(pady=5)

# Convert button & result label
tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()