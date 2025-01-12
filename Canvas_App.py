import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Drawing App")

        # Current settings
        self.current_color = "black"
        self.current_tool = "pencil"

        # Create canvas
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Tool buttons frame
        self.tool_frame = tk.Frame(root, padx=5, pady=5)
        self.tool_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Add drawing tools
        self.add_tool_button("Pencil", self.set_tool)
        self.add_tool_button("Rectangle", self.set_tool)
        self.add_tool_button("Circle", self.set_tool)

        # Add color buttons
        colors = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray"]
        for color in colors:
            self.add_color_button(color)

        # Clear canvas button
        clear_button = tk.Button(self.tool_frame, text="Clear", command=self.clear_canvas)
        clear_button.pack(pady=10, fill=tk.X)

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.start_x = None
        self.start_y = None
        self.current_shape = None

    def add_tool_button(self, text, command):
        button = tk.Button(self.tool_frame, text=text, command=lambda t=text.lower(): command(t))
        button.pack(pady=2, fill=tk.X)

    def add_color_button(self, color):
        button = tk.Button(self.tool_frame, bg=color, command=lambda c=color: self.set_color(c), width=3)
        button.pack(pady=2)

    def set_tool(self, tool):
        self.current_tool = tool

    def set_color(self, color):
        self.current_color = color

    def start_drawing(self, event):
        self.start_x = event.x
        self.start_y = event.y

        if self.current_tool in ["rectangle", "circle"]:
            if self.current_tool == "rectangle":
                self.current_shape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.current_color)
            elif self.current_tool == "circle":
                self.current_shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.current_color)

    def draw(self, event):
        if self.current_tool == "pencil":
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.current_color, width=2)
            self.start_x, self.start_y = event.x, event.y
        elif self.current_tool in ["rectangle", "circle"] and self.current_shape:
            self.canvas.coords(self.current_shape, self.start_x, self.start_y, event.x, event.y)

    def stop_drawing(self, event):
        self.start_x = None
        self.start_y = None
        self.current_shape = None

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
