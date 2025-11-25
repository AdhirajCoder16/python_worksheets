import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def angle_with(self, other):
        dot_prod = self.dot(other)
        mag1 = self.magnitude()
        mag2 = other.magnitude()
        if mag1 == 0 or mag2 == 0:
            return 0
        cos_theta = dot_prod / (mag1 * mag2)
        return math.acos(min(1, max(-1, cos_theta)))

    def projection_onto(self, other):
        other_mag_sq = other.x**2 + other.y**2
        if other_mag_sq == 0:
            return Vector(0,0)
        scale = self.dot(other) / other_mag_sq
        return Vector(other.x * scale, other.y * scale)

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

# Example usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print("Addition:", v1 + v2)
print("Magnitude of v1:", v1.magnitude())
print("Dot product:", v1.dot(v2))
print("Angle (radians):", v1.angle_with(v2))
print("Projection of v1 on v2:", v1.projection_onto(v2))
