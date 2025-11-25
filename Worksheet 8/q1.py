import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def midpoint(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def line_equation(self, other):
        if self.x == other.x:
            return f"x = {self.x}"
        m = (other.y - self.y) / (other.x - self.x)
        c = self.y - m * self.x
        return f"y = {m}x + {c}"

    def reflect_over_line(self, A, B):
        if A.x == B.x:
            x_r = 2 * A.x - self.x
            y_r = self.y
        elif A.y == B.y:
            x_r = self.x
            y_r = 2 * A.y - self.y
        else:
            m = (B.y - A.y) / (B.x - A.x)
            c = A.y - m * A.x
            d = (self.x + (self.y - c) * m) / (1 + m**2)
            x_r = 2 * d - self.x
            y_r = 2 * d * m - self.y + 2 * c
        return Point(x_r, y_r)

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

# Example use
A = Point(1, 2)
B = Point(3, 4)
C = Point(5, 1)

print("Distance:", A.distance(B))
print("Midpoint:", A.midpoint(B))
print("Line Equation:", A.line_equation(B))
print("Reflection of C over AB:", C.reflect_over_line(A, B))
