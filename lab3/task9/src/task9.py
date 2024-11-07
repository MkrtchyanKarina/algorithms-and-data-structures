from random import randint


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def create_new_dots(count, start, end):
    dots = []
    for i in range(count):
        dots.append(Dot(randint(start, end), randint(start, end)))
    return dots


def shortest_distance(dots, n):
    dots = sorted(dots, key=lambda point: point.x)
    return separation(dots, n)


def separation(dots, n):
    if n <= 3:
        return slow_shortest_distance(dots, n)
    middle = n // 2
    mid_dot = dots[middle]
    dl = separation(dots[:middle], middle)
    dr = separation(dots[middle:], n - middle)
    d = min(dl, dr)
    strip = []
    for i in range(n):
        if abs(dots[i].x - mid_dot.x) < d:
            strip.append(dots[i])
    return min(d, centre_dots(strip, len(strip), d))


def centre_dots(strip, size, d):
    min_dist = d
    strip = sorted(strip, key=lambda dot: dot.y)

    for i in range(size):
        for j in range(i + 1, size):
            if (strip[j].y - strip[i].y) >= min_dist:
                break
            min_dist = min(min_dist, euclidean_dist(strip[i], strip[j]))
    return min_dist


def euclidean_dist(dot1, dot2):
    return ((dot1.x - dot2.x) ** 2 + (dot1.y - dot2.y) ** 2)**0.5


def slow_shortest_distance(dots, n):
    min_dist = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, euclidean_dist(dots[i], dots[j]))
    return min_dist


if __name__ == "__main__":
    dots = [Dot(x=2, y=3), Dot(x=12, y=30),
            Dot(x=40, y=50), Dot(x=5, y=1), Dot(x=12, y=10), Dot(x=3, y=4)]
    n = len(dots)
    print(shortest_distance(dots, n))