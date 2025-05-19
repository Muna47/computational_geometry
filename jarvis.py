"""computing hull point using jarvis march alg"""

import math
eps = 1e-9

def equal(p1, p2):
    dx = abs(p1[0]-p2[0])
    dy = abs(p1[1]-p2[1])
    return dx < eps and dy < eps

def distance(p1, p2):
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    return (dx*dx + dy*dy) ** 0.5

def cross(ab, ac):
    return ab[0]*ac[1] - ab[1]*ac[0]

def orientation(A, B, point):
    AB = [B[0]-A[0], B[1]-A[1]]
    AP = [point[0]-A[0], point[1]-A[1]]
    cr = cross(AB, AP)
    if cr < -eps: return -1
    elif cr > eps: return 1
    else: return 0 

def jarvis(points):
    hull = []
    p = min(points, key= lambda p: (p[0], p[1]))
    while True:
        hull.append(p)
        q =  next((point for point in points if not equal(p, point)), None)
        if q == None: break
        for r in points:
            if equal(p, r): continue
            o = orientation(p, q, r)
            if o == -1 or (o == 0 and distance(p, r) > distance(p, q)):
                q = r
        p = q
        if equal(p, hull[0]): break
    return hull

n = int(input("number of points: "))
points = []
for _ in range(n):
    x, y = map(float, input("enter points: ").split())
    points.append((x, y))
hull = jarvis(points)
print(hull)