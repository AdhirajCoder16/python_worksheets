# 1.
```py
def diff_17(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return abs(n - 17)

```
# 2.
```py
def test_range(n):
    return (100 <= n <= 1000) or (n == 2000)
```

# 3.
```py
def reverse_string(s):
    return s[::-1]
```


# 4.
```py
def count_case(s):
    counts = {"UPPER": 0, "LOWER": 0}
    for ch in s:
        if ch.isupper():
            counts["UPPER"] += 1
        elif ch.islower():
            counts["LOWER"] += 1
    return counts
```


# 5.
```py
def distinct_list(lst):
    return list(set(lst))
```

# 6.
```py
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]
```

# 7.
```py
def robot():
    def move():
        print("Robot is moving")
    move()
```


# 8.
```py
def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student.__doc__ = "This function shows student details."

```
# 9.
```py
def move_robot(x, y, direction):
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return x, y
```

# 10.
```py
def classify_temperature(temp):
    if temp < 15:
        return "Cold"
    elif 15 <= temp <= 30:
        return "Moderate"
    else:
        return "Hot"

```
# 11.
```py
def is_goal_reached(path):
    x, y = 0, 0
    for move in path:
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
    return (x, y) == (2, 0)
```

# 12.
```py
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.student_name)
        print("Class:", self.student_class)
```

# 13.
```py
student1 = Student(1, "Rahul", "12A")
student2 = Student(2, "Priya", "12B")

print("Student 1 ->", vars(student1))
print("Student 2 ->", vars(student2))
```

# 14.
```py
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

```
# 15.
```py
class MyString:
    def get_string(self):
     self.text = input("Enter a string: ")

    def print_string(self):
        print(self.text.upper())
```

# 16.
```py
class Robot:
    def __init__(self, name, task, battery_level=100):
        self.name = name
        self.task = task
        self.battery_level = battery_level

    def perform_task(self):
        print(self.name, "is performing:", self.task)
        self.battery_level -= 10

    def recharge(self):
        self.battery_level = 100
        print(self.name, "is recharged!")

    def status(self):
        print("Name:", self.name)
        print("Task:", self.task)
        print("Battery:", self.battery_level, "%")
```
