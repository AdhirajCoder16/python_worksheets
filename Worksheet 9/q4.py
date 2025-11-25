import tkinter as tk

root = tk.Tk()
root.title("Moving Point")

canvas = tk.Canvas(root, width=400, height=100)
canvas.pack()

x, y, r = 10, 50, 5
point = canvas.create_oval(x - r, y - r, x + r, y + r, fill='red')

def move_point():
    
    x += 5
    if x > 400 + r:
        x = -r
    canvas.coords(point, x - r, y - r, x + r, y + r)
    root.after(50, move_point)

move_point()
root.mainloop()
