class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

def cross(p1, p2):
    return p1.x*p2.y - p1.y*p2.x

t = int(input())
for _ in range(t):
    a_x, a_y, b_x, b_y, point_x, point_y = map(int, input().split())
    a = Point(a_x, a_y)
    b = Point(b_x, b_y)
    point = Point(point_x, point_y)

    ab = b - a
    aPoint = point - a 

    if cross(ab, aPoint) > 0:
        print("LEFT")
    elif cross(ab, aPoint) < 0:
        print("RIGHT")
    else:
        print("TOUCH")
