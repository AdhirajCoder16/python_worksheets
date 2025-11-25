import tkinter as tk

points = [(20, 50), (100, 120), (180, 90), (250, 150)]

root = tk.Tk()
root.title("Robot Path")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Flatten the points list for create_line
flat_points = [coord for point in points for coord in point]

canvas.create_line(flat_points, fill='blue', width=3)

root.mainloop()
