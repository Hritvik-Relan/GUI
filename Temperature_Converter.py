import tkinter as tk
from tkinter import ttk

# Function to convert temperatures
def convert_temperature():
    try:
        value = float(entry_temperature.get())
        if combo_from.get() == "Celsius" and combo_to.get() == "Fahrenheit":
            converted = (value * 9/5) + 32
        elif combo_from.get() == "Fahrenheit" and combo_to.get() == "Celsius":
            converted = (value - 32) * 5/9
        else:
            converted = value  # Same unit selected
        
        label_result.config(text=f"Converted Temperature: {converted:.2f}")
    except ValueError:
        label_result.config(text="Please enter a valid number.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

# Input field for temperature
label_temperature = ttk.Label(root, text="Enter Temperature:")
label_temperature.pack(pady=5)
entry_temperature = ttk.Entry(root)
entry_temperature.pack(pady=5)

# Dropdown to select "From" unit
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit"])
combo_from.current(0)  # Default to "Celsius"
combo_from.pack(pady=5)

# Dropdown to select "To" unit
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit"])
combo_to.current(1)  # Default to "Fahrenheit"
combo_to.pack(pady=5)

# Button to convert
button_convert = ttk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=10)

# Label to display result
label_result = ttk.Label(root, text="")
label_result.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
