import tkinter as tk

window = tk.Tk()
window.config(bg="yellow")
window.title("Robot control panel")
window.geometry('500x400')

canvas = tk.Canvas(window, width=500, height=400, bg="yellow")
canvas.pack()

# Draw the rectangle (robot body)
canvas.create_rectangle(200, 120, 300, 220, fill="gray", outline="black")

# Draw the wheels (circles)
canvas.create_oval(190, 215, 220, 245, fill="black")  # Left wheel
canvas.create_oval(280, 215, 310, 245, fill="black")  # Right wheel

window.mainloop()
