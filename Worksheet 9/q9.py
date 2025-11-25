import tkinter as tk
import math

def circle_intersection(c1, r1, c2, r2):
    x0, y0 = c1
    x1, y1 = c2
    dx, dy = x1 - x0, y1 - y0
    d = math.hypot(dx, dy)
    if d > r1 + r2 or d < abs(r1 - r2):
        return None
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    xm = x0 + a * dx / d
    ym = y0 + a * dy / d
    xs1 = xm + h * dy / d
    ys1 = ym - h * dx / d
    xs2 = xm - h * dy / d
    ys2 = ym + h * dx / d
    return (xs1, ys1), (xs2, ys2)

root = tk.Tk()
root.title("Four-Bar Mechanism")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()


A = (150, 300)
D = (400, 300)
L2 = 120  
L3 = 150  
L4 = 130 
theta_deg = 30
theta = math.radians(theta_deg)


Bx = A[0] + L2 * math.cos(theta)
By = A[1] - L2 * math.sin(theta)
B = (Bx, By)


circles = circle_intersection(B, L3, D, L4)
if circles:
    C = circles[0]  
else:
    C = None


r = 5
for point in [A, B, C, D]:
    if point:
        canvas.create_oval(point[0]-r, point[1]-r, point[0]+r, point[1]+r, fill='black')


if C:
    canvas.create_line(A[0], A[1], B[0], B[1], fill='red', width=3)     
    canvas.create_line(B[0], B[1], C[0], C[1], fill='blue', width=3)    
    canvas.create_line(C[0], C[1], D[0], D[1], fill='green', width=3)  
    canvas.create_line(D[0], D[1], A[0], A[1], fill='orange', width=3) 

root.mainloop()
