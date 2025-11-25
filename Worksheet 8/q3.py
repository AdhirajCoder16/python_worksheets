import math

class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point1[0] - self.point2[0])**2 + (self.point1[1] - self.point2[1])**2)

    def closest_point(self, point):
        x1, y1 = self.point1
        x2, y2 = self.point2
        x3, y3 = point
        dx = x2 - x1
        dy = y2 - y1
        if dx == dy == 0:
            return self.point1
        t = ((x3 - x1) * dx + (y3 - y1) * dy) / (dx*dx + dy*dy)
        t = max(0, min(1, t))
        return (x1 + t * dx, y1 + t * dy)

    def distance_to_point(self, point):
        cp = self.closest_point(point)
        return math.sqrt((point[0] - cp[0])**2 + (point[1] - cp[1])**2)

# Example usage
seg = Segment((1, 2), (4, 6))
point = (3, 3)
print("Length of segment:", seg.length())
print("Closest point to", point, ":", seg.closest_point(point))
print("Distance from point to segment:", seg.distance_to_point(point))
