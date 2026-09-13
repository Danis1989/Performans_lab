import sys


def pos_points_ellipse(center1, center2, ellipse1, ellipse2, point):
    res = []

    for i in point: # Расчитываем положение для каждой из точек(которых может быть не менее 100).
        point1, point2 = i # Разделяем координаты точек на отдельные элементы.
        pos = (pow(point1 - center1, 2) / pow(ellipse1, 2)) + (pow(point2 - center2, 2) / pow(ellipse2, 2))

        if pos == 1:
            r = 0
        elif pos < 1:
            r = 1
        else:
            r = 2
        res.append(r)
    return res


def main():
    if len(sys.argv) < 3 or sys.argv != ['task2.py', 'file1.txt', 'file2.txt']:
        print("Для запуска программы введите: python(или python3) task2.py file1.txt file2.txt")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    with open(file1) as f1:
        cen1, cen2, ell1, ell2 = map(int, f1.read().split())

    with open(file2) as f2:
        points = []
        for i in f2:
            points.append(list(map(int, i.strip().split())))

    print(*pos_points_ellipse(cen1, cen2, ell1, ell2, points), sep='\n')


if __name__ == '__main__':
    main()
