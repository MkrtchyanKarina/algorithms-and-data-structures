import pathlib
import sys

sys.setrecursionlimit(10**8)


def shortest_distance(count: int, dots: list, d_left=10**8, d_right=10**8, global_min=10 ** 8):
    dots.sort()
    if len(dots) == 2:
        return distance(dots)
    middle = count//2
    coef = count % 2
    left_area = dots[:middle+coef]

    count_left = len(left_area)
    right_area = dots[middle:]
    count_right = len(right_area)
    # print(left_area, right_area)
    if count_left > 2:
        global_min = min(shortest_distance(count_left, left_area, d_left, d_right), global_min)
    elif count_left == 2:
        d_left = distance(left_area)
    if count_right > 2:
        global_min = min(shortest_distance(count_right, right_area, d_left, d_right), global_min)
    elif count_right == 2:
        d_right = distance(right_area)


    local_min = min(d_left, d_right)
    middle_val = dots[middle][0]
    left_centre_dots = [d for d in dots if middle_val-local_min <= d[0] <= middle_val]
    right_centre_dots = [d for d in dots if middle_val < d[0] <= middle_val+local_min]

    left_centre_dots.sort(key=lambda x: x[1])
    right_centre_dots.sort(key=lambda x: x[1])
    local_min = min(local_min, centre_min_dist(left_centre_dots, len(left_centre_dots), right_centre_dots, len(right_centre_dots), 0, 0, local_min))
    global_min = min(global_min, local_min)
    return global_min


def distance(dots:list):
    dot1, dot2 = dots
    x1, y1 = dot1
    x2, y2 = dot2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def centre_min_dist(left_dots, len_l, right_dots, len_r, index_l, index_r, d_min):
    if index_l < len_l and index_r < len_r:
        d_min = min(d_min, distance([left_dots[index_l], right_dots[index_r]]))
        if index_l + 1 < len_l and index_r + 1 < len_r:
            if left_dots[index_l + 1][1] < right_dots[index_r + 1][1]:
                centre_min_dist(left_dots, len_l, right_dots, len_r, index_l+1, index_r, d_min)
            elif left_dots[index_l + 1][1] > right_dots[index_r + 1][1]:
                centre_min_dist(left_dots, len_l, right_dots, len_r, index_l, index_r+1, d_min)
            else:
                centre_min_dist(left_dots, len_l, right_dots, len_r, index_l+1, index_r, d_min)
                centre_min_dist(left_dots, len_l, right_dots, len_r, index_l, index_r+1, d_min)
                centre_min_dist(left_dots, len_l, right_dots, len_r, index_l+1, index_r+1, d_min)
    return d_min


def read_txt(file_name):
    file = open(pathlib.Path(pathlib.Path(__file__).parent.parent, 'txtf', file_name), 'r')
    count = int(file.readline())
    dots = []
    for i in range(count):
        x, y = list(map(int, file.readline().split(" ")))
        dots.append((x, y))
    print(shortest_distance(count, dots))

if __name__ == "__main__":
    read_txt('task9.txt')
