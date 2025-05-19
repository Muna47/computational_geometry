import math
eps = 1e-9

def cross(ab, ac):
    return ab[0]*ac[1] - ab[1]*ac[0]

def pointOnSegment(A, B, point):
    ab = [B[0]-A[0], B[1]-A[1]]
    ac = [point[0]-A[0], point[1]-A[1]]
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
    else: return 0 if pointOnSegment(A, B, point) else -1

def pointInConvex(points, point):
    lo = 0
    hi = len(points) - 1
    
    if pointOnSegment(points[0], points[1], point) or pointOnSegment(points[0], points[-1], point): 
        print("Point lies on the boundary of polygon")
        return

    while lo + 1 < hi:
        mid = lo + (hi-lo) // 2
        o = orientation(points[0], points[mid], point)
        if o < -eps: hi = mid
        else: lo = mid

    A, B, C = points[0], points[lo], points[hi]
    o1 = orientation(A, B, point)
    o2 = orientation(B, C, point)
    o3 = orientation(C, A, point)

    if o1 < -eps or o2 < -eps or o3 < -eps:
        print("Point lies outside of the polygon")
    elif o1 == 0 or  o2 == 0 or o3 == 0: 
        print("Point lies on the boundary of polygon")
    else: 
        print("Point lies inside of the polygon")

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