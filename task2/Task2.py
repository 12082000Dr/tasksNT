from math import sqrt

def distance(p1, p2):
    """Вычиление расстояния между точками"""
    return sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

with open(input()) as file_centre, open(input()) as file_point:
    centre = file_centre.read().split('\n')
    points = file_point.read().split('\n')

centre_rad = [i.split(' ') for i in centre]
points = [i.split(' ') for i in points]

centre = [float(centre_rad[0][0]), float(centre_rad[0][1])]
rad = float(centre_rad[1][0])

result = []

for i, j in points:
    point = [float(i), float(j)]
    dist = distance(point, centre)
    if dist == rad:
        result.append(0)
    elif dist < rad:
        result.append(1)
    elif dist > rad:
        result.append(2)
        
print(*result, sep='\n')
