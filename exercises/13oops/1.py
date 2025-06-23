class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return (self.x, self.y)

    def dist_from_origin(self):
        dist = (self.x**2 + self.y**2) ** 0.5
        self.dist = dist
        return self.dist

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def __gt__(self, other):
        return self.dist > other.dist

    def __ge__(self, other):
        if self.dist >= other.dist:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.dist < other.dist:
            return True
        else:
            return False

    def __le__(self, other):
        if self.dist <= other.dist:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.dist == other.dist:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.dist != other.dist:
            return True
        else:
            return False


p1 = Point(1, 1)
print(f"{p1.get_point()} distance from origin  = {p1.dist_from_origin()}")
p2 = Point(2, 2)
print(f"{p2.get_point()} distance from origin  = {p2.dist_from_origin()}")
print(f"{p1.get_point()} + {p2.get_point()} = {p1 + p2}")
print(f"{p1.get_point()} - {p2.get_point()} = {p1 - p2}")
print(f"{p1.get_point()} is more farther from origin than {p2.get_point()} = {p1 > p2}")
print(f"{p1.get_point()} is less farther from origin than {p2.get_point()} = {p1 < p2}")
print(
    f"{p1.get_point()} is more or equally farther from origin than {p2.get_point()} = {p1 >= p2}"
)
print(
    f"{p1.get_point()} is less or equally farther from origin than {p2.get_point()} = {p1 <= p2}"
)
print(
    f"{p1.get_point()} is equally farther from origin than {p2.get_point()} = {p1 == p2}"
)
print(
    f"{p1.get_point()} is not equally farther from origin than {p2.get_point()} = {p1 != p2}"
)
