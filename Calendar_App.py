import tkinter as tk
from tkinter import ttk
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")

        # Dropdowns for year and month selection
        self.year_label = tk.Label(root, text="Year:")
        self.year_label.grid(row=0, column=0, padx=5, pady=5)

        self.year_entry = ttk.Entry(root, width=10)
        self.year_entry.grid(row=0, column=1, padx=5, pady=5)
        self.year_entry.insert(0, str(calendar.datetime.datetime.now().year))

        self.month_label = tk.Label(root, text="Month:")
        self.month_label.grid(row=0, column=2, padx=5, pady=5)

        self.month_combobox = ttk.Combobox(root, values=[
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])
        self.month_combobox.grid(row=0, column=3, padx=5, pady=5)
        self.month_combobox.set(calendar.month_name[calendar.datetime.datetime.now().month])

        # Display button
        self.display_button = ttk.Button(root, text="Display Calendar", command=self.display_calendar)
        self.display_button.grid(row=0, column=4, padx=5, pady=5)

        # Calendar output
        self.calendar_text = tk.Text(root, width=40, height=15)
        self.calendar_text.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

        self.display_calendar()  # Display current month's calendar at startup

    def display_calendar(self):
        year = self.year_entry.get()
        month = self.month_combobox.get()

        if not year.isdigit():
            self.calendar_text.delete(1.0, tk.END)
            self.calendar_text.insert(tk.END, "Invalid year. Please enter a valid number.")
            return

        year = int(year)
        try:
            month_number = list(calendar.month_name).index(month)
        except ValueError:
            self.calendar_text.delete(1.0, tk.END)
            self.calendar_text.insert(tk.END, "Invalid month. Please select a valid month.")
            return

        cal = calendar.TextCalendar()
        month_calendar = cal.formatmonth(year, month_number)

        self.calendar_text.delete(1.0, tk.END)
        self.calendar_text.insert(tk.END, month_calendar)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
