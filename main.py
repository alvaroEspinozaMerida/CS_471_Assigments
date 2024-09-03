import math

test_data1 = [(1, 3, .7), (2, 3, .4), (3, 3, .9)]
test_data2 = [(1.5, 1.5, 1.3), (4, 4, .7)]
test_data3 = [(.5, .5, .5), (1.5, 1.5, 1.1), (.7, .7, .4), (4, 4, .7)]
test_data4 = [(0, 0, 1), (2, 0, 1), (4, 0, 1)]
test_data5 = [(0, 0, 1), (5, 0, 1), (10, 0, 1)]


def distance(a,b):
    return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

def check_intersect(point1, point2):

    return (distance(point1, point2) < (point1[2]+point2[2]) and distance(point1, point2) > (point1[2]-point2[2])) or (distance(point1,point2) == (point1[2]+point2[2]) or distance(point1,point2) == (point1[2]-point2[2]))


def check_cluster(points):

    current = points[0]
    for i in range(1,len(points)):
        if not check_intersect(current, points[i]):
            return False
        else:
            current = points[i]

    return True


print(check_cluster(test_data1))
print(check_cluster(test_data2))
print(check_cluster(test_data3))
print(check_cluster(test_data4))
print(check_cluster(test_data5))





