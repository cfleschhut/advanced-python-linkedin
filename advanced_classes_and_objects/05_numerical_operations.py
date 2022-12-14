class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point x:{self.x}, y:{self.y}>"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


p1 = Point(10, 20)
p2 = Point(30, 30)

print(p1 + p2)
print(p1 - p2)

p1 += p2
print(p1)
