import tkinter as tk

window = tk.Tk()
window.config(bg="yellow")
window.title("Robot control panel")
window.geometry('500x400')

canvas = tk.Canvas(window, width=500, height=400, bg="yellow")
canvas.pack()

path = [(20, 50), (100, 120), (180, 90), (250, 150)]


canvas.create_line(path, fill="blue", width=3)

window.mainloop()
