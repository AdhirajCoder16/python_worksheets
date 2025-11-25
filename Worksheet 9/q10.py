import tkinter as tk

class RobotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Path Tracker")

        self.canvas = tk.Canvas(root, width=500, height=400, bg='white')
        self.canvas.pack()

        self.radius = 10
        self.x, self.y = 250, 200
        self.robot = self.canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                             self.x + self.radius, self.y + self.radius,
                                             fill='blue')
        self.path_points = [(self.x, self.y)]

        self.canvas.bind_all('<KeyPress>', self.key_press)

        self.reset_btn = tk.Button(root, text="RESET", command=self.reset_path)
        self.reset_btn.pack(pady=10)

    def key_press(self, event):
        dx, dy = 0, 0
        if event.keysym == 'Up':
            dy = -5
        elif event.keysym == 'Down':
            dy = 5
        elif event.keysym == 'Left':
            dx = -5
        elif event.keysym == 'Right':
            dx = 5
        if dx != 0 or dy != 0:
            self.move_robot(dx, dy)

    def move_robot(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.robot, dx, dy)
        self.path_points.append((self.x, self.y))
        self.draw_path()

    def draw_path(self):
        self.canvas.delete('path_line')
        if len(self.path_points) > 1:
            self.canvas.create_line(self.path_points, fill='red', width=2, tags='path_line')

    def reset_path(self):
        self.path_points = [(self.x, self.y)]
        self.canvas.delete('path_line')

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotApp(root)
    root.mainloop()
