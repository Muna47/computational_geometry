import math
eps = 1e-9

def cross(ab, ac):
    return ab[0]*ac[1] - ab[1]*ac[0]

def pointOnSegment(ab, ac):
    if ab[0] != 0: 
        t = ac[0] / ab[0]
    else:
        t = ac[1] / ab[1]

    return 0-eps <= t <= 1+eps
    
    
def orientation(A, B, point):
    AB = [B[0]-A[0], B[1]-A[1]]
    AP = [point[0]-A[0], point[1]-A[1]]
    cr = cross(AB, AP)
    if cr < -eps: return -1
    elif cr > eps: return 1
    else: return 0 if pointOnSegment(AB, AP) else -1

def pointInConvex(points, point):
    n = len(points)
    for i in range(n):
        A = points[i]
        B = points[(i+1) % n]
        o = orientation(A, B, point)
        if o == -1:
            print("point is outside the polygon")
            return
    print("point is inside the polygon")

n = int(input("number of points: "))
points = []
for _ in range(n):
    x, y = map(float, input("enter points: ").split())
    points.append((x, y))

c_x = sum(p[0] for p in points) / len(points)
c_y = sum(p[1] for p in points) / len(points)

points = sorted(points, key= lambda p: math.atan2((p[1]-c_y), (p[0]-c_x)))
x, y = map(float, input("enter x, y of a point: ").split())
point = (x, y)
pointInConvex(points, point)