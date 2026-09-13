import sys


def min_num_moves(mass):
    mass.sort()  # Отсортируем массив для нахождения медианного числа.
    ind = len(mass) // 2  # Определяем индекс медианного числа.
    res = 0  # Для хранения результата.
    for i in mass:
        res += mass[ind] - i if i < mass[ind] else i - mass[ind]  # Для удобства,из большего всегда вычитаем меньшее.
        if res > 20:  # Если промежуточный результат превысит число 20, досрочно выходим из цикла.
            res = '20 ходов недостаточно для приведения всех элементов массива к одному числу'
            break

    return res


def main():  # Проверяем, что аргумент передан.
    if len(sys.argv) < 2:
        print("Для запуска программы введите: python(или python3) task4.py test1. Доступны файлы: test1, test2, test3")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename) as f:  # Читаем массив из файла. По умолчанию установлен на чтение.
        nums = [int(x) for x in f.read().split()]  # Разбиваем весь текст на числа.

    print(min_num_moves(nums))


if __name__ == "__main__":
    main()
