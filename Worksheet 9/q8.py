import tkinter as tk

root = tk.Tk()
root.title("Robot Straight Line Movement")

canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

x, y, r = 50, 200, 10
target_x = 450
velocity = 5  

robot = canvas.create_oval(x - r, y - r, x + r, y + r, fill='red')

def move_robot():
  
    if x < target_x:
        x += velocity
        canvas.coords(robot, x - r, y - r, x + r, y + r)
        root.after(50, move_robot)

move_robot()
root.mainloop()
