from config import SHEET


def append_data(new_row):
    """
    Добавляет новую строку с данными в таблицу Google Sheets.

    Параметры:
    new_row (list): Список значений, которые нужно добавить в новую строку таблицы.
    """
    try:
        SHEET.append_row(new_row)
    except Exception as e:
        print("Ошибка при добавлении данных: ", e)


def read_data():
    """
    Считывает все данные из таблицы Google Sheets и выводит их в консоль.
    """
    try:
        data = SHEET.get_all_values()
        for row in data:
            print(row)
    except Exception as e:
        print("Ошибка при чтении данных: ", e)


def update_cell(row, col, value):
    """
    Обновляет значение в указанной ячейке таблицы Google Sheets.

    Параметры:
    row (int): Номер строки, в которой находится ячейка.
    col (int): Номер колонки, в которой находится ячейка.
    value (str): Новое значение для ячейки.
    """
    try:
        SHEET.update_cell(row, col, value)
    except Exception as e:
        print("Ошибка при обновлении данных в ячейке: ", e)


def update_row_numbers():
    """
    Обновляет номера строк в таблице Google Sheets.
    """
    try:
        data = SHEET.get_all_values()
        for index in range(1, len(data)):
            SHEET.update_cell(index + 1, 1, str(index))
    except Exception as e:
        print("Ошибка при обновлении номеров строк: ", e)


def delete_row(row_number):
    """
    Удаляет строку по указанному номеру из таблицы Google Sheets.

    Параметры:
    row_number (int): Номер строки, которую нужно удалить.
    """
    try:
        SHEET.delete_rows(row_number)
    except Exception as e:
        print("Ошибка при удалении данных: ", e)
