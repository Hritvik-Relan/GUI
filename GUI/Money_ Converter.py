import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

# Tkinter Base Functions
root = tk.Tk()
root.geometry("400x300")
root.title("Money Conversions")

# Currency conversion rates
conversion_rates = {
    "CAD": 1.00,
    "USD": 0.70,
    "GBP": 0.56,
    "Euro": 0.67,
    "JPY": 109.47,
    "KRW": 1015.83,
    "INR": 59.31,
}

# Value Entry
tk.Label(root, text="Enter Amount:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_amount = tk.Entry(root, width=10)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

# Combobox for currencies
tk.Label(root, text="Select Currency:").grid(row=1, column=0, padx=10, pady=10)
currency_selector = ttk.Combobox(root, values=list(conversion_rates.keys()), state="readonly", width=10)
currency_selector.grid(row=1, column=1, padx=10, pady=10)
currency_selector.set("CAD")

# Output Label
result_label = tk.Label(root, text="Converted Value: N/A")
result_label.grid(row=3, column=0, columnspan=2, pady=20)

# Conversion Function
def convert():
    try:
        # Get the entered value and the selected currency
        amount = float(entry_amount.get())
        selected_currency = currency_selector.get()
        
        if selected_currency not in conversion_rates:
            messagebox.showerror("Error", "Please select a valid currency.")
            return

        # Convert and display the result
        conversion_rate = conversion_rates[selected_currency]
        converted_value = amount * conversion_rate
        result_label.config(text=f"Converted Value: {converted_value:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered. Please enter a numeric value.")

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
