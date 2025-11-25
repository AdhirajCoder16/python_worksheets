import tkinter as tk

def move_robot(dx, dy):
    canvas.move(robot, dx, dy)

root = tk.Tk()
root.title("Robot Movement")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

robot = canvas.create_oval(140, 140, 160, 160, fill='green')

frame = tk.Frame(root)
frame.pack()

btn_up = tk.Button(frame, text="Up", command=lambda: move_robot(0, -10))
btn_up.grid(row=0, column=1)

btn_left = tk.Button(frame, text="Left", command=lambda: move_robot(-10, 0))
btn_left.grid(row=1, column=0)

btn_down = tk.Button(frame, text="Down", command=lambda: move_robot(0, 10))
btn_down.grid(row=1, column=1)

btn_right = tk.Button(frame, text="Right", command=lambda: move_robot(10, 0))
btn_right.grid(row=1, column=2)

root.mainloop()
