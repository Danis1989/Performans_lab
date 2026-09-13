import sys

def сircular_array_func(length_array, interval_array):
    mass = [i for i in range(1, length_array + 1)] * 2 # Создаем массив.
    start, stop = 0, interval_array                    # Начальная и конечная точка интервала для старта.
    res = []                                           # Окончательный результат.
    ms = [0]                                           # Для хранения текущего интервала.

    while ms[-1] != mass[0]: # Пока последний элемент текущего интервала(ms) не станет равен первому элементу основного массива(mass):
        ms = mass[start:stop]
        ind = mass.index(ms[-1]) # Находим индекс элемента в основном массиве на основе последнего элемента текущего интервала.
        res.append(ms[0])
        start = ind
        stop = start + interval_array
    return res

if len(sys.argv) != 5:
    print("Ошибка: нужно передать ровно 4 аргумента")
    print("Для запуска программы введите: python3( или python) script.py 6 3 5 4 (Цифры вводите свои.)")
    sys.exit(1)

n1, m1, n2, m2 = map(int, sys.argv[1:5])


print(*сircular_array_func(n1, m1), *сircular_array_func(n2, m2), sep='')