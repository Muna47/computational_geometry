INF = float('inf')

def calculateDistance(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return (dx * dx + dy * dy) ** 0.5

def closestPair(n, points):
    if n <= 1: return INF
    if n == 2: return calculateDistance(points[0], points[1])

    #if duplicate points return 0
    for i in range(1, n):
        if points[i] == points[i-1]:
            return 0
    
    midIndex = n // 2
    leftPoints = points[:midIndex]
    rightPoints = points[midIndex:]

    #partition
    leftDistance = closestPair(len(leftPoints), leftPoints)
    rightDistance = closestPair(len(rightPoints), rightPoints)
    minDistance = min(leftDistance, rightDistance)
    
    stripPoints = []
    midX = points[midIndex][0]
    for point in points:
        if abs(point[0] - midX) < minDistance:
            stripPoints.append(point)
    
    stripPoints = sorted(stripPoints, key= lambda p: p[1])
    m = len(stripPoints)
    for i in range(m):
        for j in range(i+1, min((i+8), m)):
            distance = calculateDistance(stripPoints[i], stripPoints[j])
            minDistance = min(distance, minDistance)
    return minDistance

n = int(input("number of points: "))
points = []
for _ in range(n):
    x, y = map(float, input("enter points: ").split())
    points.append((x, y))

points = sorted(points, key= lambda p: (p[0], p[1]))
distance = closestPair(n, points)
print(f"Minimum distance: {distance}")