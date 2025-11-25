import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Robot Control Panel")
window.geometry("500x400")
window.configure(bg="yellow")

canvas = tk.Canvas(window, width=500, height=400, bg="yellow")
canvas.pack()

radius = 1  
x, y = 100, 100
canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="black")

window.mainloop()
