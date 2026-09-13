from json import *
from sys import *


def json_load(filepath): # Загружаем JSON из файла.
    with open(filepath, 'r', encoding='utf-8') as f:
        return load(f)


def json_save(data, filepath): # Сохраняем данные в JSON файл.
    with open(filepath, 'w', encoding='utf-8') as f:
        dump(data, f, indent=2, ensure_ascii=False)


def build_values_map(values_data): # Формируем словарь {id: value} из values.json.
                                   # Предполагаем что values.json — это список объектов с полями id и value.
    values_map = {}
    # Если values.json — объект с полем values (список внутри)
    if isinstance(values_data, dict):
        values_list = values_data.get('values', [])# Если ключа нет, то вернётся пустой список [] (защита от ошибки).
        if isinstance(values_list, list):# Защита от некорректных данных. Например, если "values": "строка".
            for i in values_list:
                if isinstance(i, dict) and 'id' in i and 'value' in i:# Если ошибок нет, создаем словарь.
                    values_map[i['id']] = i['value']

    return values_map


def fill_report(tests_structure, values_map): # Рекурсивно обходит структуру tests.json и заполняет поле value
                                              # на основе values_map.


    if isinstance(tests_structure, list): # Если это список — обрабатываем каждый элемент.
        return [fill_report(item, values_map) for item in tests_structure]

    if isinstance(tests_structure, dict): # Если это словарь — обрабатываем его поля.
        res = {}

        for key, value in tests_structure.items():
            if key == 'value' and 'id' in tests_structure: # Заполняем value по id, если оно есть в values_map.
                test_id = tests_structure['id']
                res[key] = values_map.get(test_id, value)
            elif key == 'values' and isinstance(value, list): # Рекурсивно обрабатываем вложенный список values.
                res[key] = fill_report(value, values_map)
            else:                                            # Остальные поля копируем как есть (рекурсивно для вложенных структур).
                res[key] = fill_report(value, values_map)

        return res

    return tests_structure # Примитивные типы возвращаем как есть.


def main():
    # Проверяем количество аргументов
    if len(argv) != 4:
        print("Для запуска программы введите: python(или python3) task3.py values.json tests.json report.json")
        exit(1)

    values_path = argv[1]
    tests_path = argv[2]
    report_path = argv[3]

    values_data = json_load(values_path) # Загружаем данные.
    tests_data = json_load(tests_path)

    values_map = build_values_map(values_data) # Cоздаем структуру значений.

    report_data = fill_report(tests_data, values_map) # Cоздаем отчёт.

    json_save(report_data, report_path)   # Сохраняем результат.

    print({report_path}) # Формируем итоговый файл report.json


if __name__ == '__main__':
    main()