from config import SHEET, COLUMN_COST, COLUMN_PRICE, COLUMN_QUANTITIES
from google_sheets_crud import append_data, update_row_numbers


def edit_row(row_number, product_name, price, quantity):
    """
    Обновляет существующие данные в строке таблицы Google Sheets.

    Параметры:
    row_number (int): Номер строки, которую нужно обновить.
    product_name (str): Новое название продукта.
    price (float): Новая цена продукта.
    quantity (int): Новое количество продукта.
    """
    try:
        cost = price * quantity

        new_row_data = [
            str(row_number),
            product_name,
            float(price),
            int(quantity),
            float(cost),
        ]

        for col_number, value in enumerate(new_row_data, start=1):
            SHEET.update_cell(row_number, col_number, value)

        print("Строка успешно изменена.")

        update_row_numbers()
    except Exception as e:
        print("Ошибка при изменении строки: ", e)


def find_rows_by_criteria(column_index, search_value):
    """
    Ищет строки в таблице Google Sheets по заданному критерию.

    Параметры:
    column_index (int): Индекс столбца, по которому производится поиск.
    search_value (str): Значение, по которому производится поиск.

    Возвращает:
    list: Список найденных строк.
    """
    try:
        data = SHEET.get_all_values()
        found_rows = []

        for row in data:
            if row[column_index] == search_value:
                found_rows.append(row)

        return found_rows
    except Exception as e:
        print("Ошибка при поиске строк: ", e)


def find_rows_by_partial_match(column_index, keyword):
    """
    Ищет строки в таблице Google Sheets по частичному совпадению в заданном столбце.

    Параметры:
    column_index (int): Индекс столбца, по которому производится поиск.
    keyword (str): Ключевое слово для поиска.

    Возвращает:
    list: Список найденных строк.
    """
    try:
        data = SHEET.get_all_values()
        found_rows = []

        for index, row in enumerate(data, start=1):
            if keyword.lower() in row[column_index].lower():
                found_rows.append([index] + row)

        return found_rows
    except Exception as e:
        print("Ошибка при поиске строк: ", e)


def is_found_rows(found_rows):
    """
    Проверяет, были ли найдены строки, и выводит их.

    Параметры:
    found_rows (list): Список найденных строк.

    Возвращает:
    bool: True, если строки были найдены, иначе False.
    """
    if found_rows:
        print("\nНайденные строки:")
        for index, row in enumerate(found_rows, start=1):
            print(f"{index}: {row}")
        return True
    else:
        print("Не найдено строк.")
        return False


def get_user_choice(found_rows):
    """
    Запрашивает у пользователя выбор строки для редактирования.

    Параметры:
    found_rows (list): Список найденных строк.

    Возвращает:
    int: Номер строки, выбранной пользователем, или None, если выбор некорректен.
    """
    choice_input = input("Выберите номер строки для редактирования: ")
    if choice_input.isdigit():
        choice_index = int(choice_input)
        if 1 <= choice_index <= len(found_rows):
            return int(found_rows[choice_index - 1][0])
        else:
            print("Некорректный выбор строки.")
    else:
        print("Ошибка: Введите корректный номер строки.")
    return None


def edit_row_by_number(search_column_index, keyword, row_number):
    """
    Изменяет строку в таблице Google Sheets по частичному совпадению в заданном столбце.

    Параметры:
    search_column_index (int): Индекс столбца для поиска.
    keyword (str): Ключевое слово для поиска.
    row_number (int): Номер строки, которую нужно изменить.
    """
    try:
        found_rows = find_rows_by_partial_match(search_column_index, keyword)
        row_to_edit = [row for row in found_rows if row[0] == row_number][0]
        product_name = row_to_edit[2]
        price = float(row_to_edit[3])
        quantity = int(row_to_edit[4])

        print(f"Текущие данные для редактирования: {row_to_edit}")
        new_product_name = input(
            "Введите новое название продукта (Enter для пропуска): "
        )
        new_price = input("Введите новую цену продукта (Enter для пропуска): ")
        new_quantity = input("Введите новое количество продукта (Enter для пропуска): ")

        if new_product_name:
            product_name = new_product_name
        if new_price:
            price = float(new_price)
        if new_quantity:
            quantity = int(new_quantity)

        edit_row(row_number, product_name, price, quantity)

        update_row_numbers()
    except Exception as e:
        print("Ошибка при редактировании строки: ", e)


def get_user_data():
    """
    Запрашивает у пользователя данные о продукте и возвращает их в виде списка.

    Возвращает:
    list: Список данных о продукте (название, цена, количество, стоимость) или None, если ввод некорректен.
    """
    try:
        product_name = input("Введите название продукта: ")
        price = float(input("Введите цену продукта: "))
        quantity = int(input("Введите количество продукта: "))
        cost = price * quantity
        return [product_name, price, quantity, cost]
    except ValueError:
        print("Ошибка: Некорректный формат данных.")
        return None


def up_user_data():
    """
    Добавляет данные о продукте, введенные пользователем, в таблицу Google Sheets.
    """
    user_data = get_user_data()
    if user_data:
        try:
            num_columns = len(SHEET.row_values(1))
            num_rows = len(SHEET.get_all_values())

            new_row = [""] * num_columns
            new_row[0] = str(num_rows)
            new_row[1:4] = user_data
            append_data(new_row)
        except Exception as e:
            print("Ошибка при обновлении данных:", e)


def quantities_analyze(quantities):
    """
    Анализирует количество продуктов в списке и выводит результаты анализа.

    Параметры:
    quantities (list): Список количеств продуктов.
    """
    try:
        min_quantity = min(quantities)
        max_quantity = max(quantities)
        total_quantity = sum(quantities)

        print(f"Общее количество всех товаров: {total_quantity}")
        print(f"Минимальное количество: {min_quantity}")
        print(f"Максимальное количество: {max_quantity}")
    except Exception as e:
        print("Ошибка при анализе количества: ", e)


def price_analyze(prices):
    """
    Анализирует цены продуктов в списке и выводит результаты анализа.

    Параметры:
    prices (list): Список цен продуктов.
    """
    try:
        min_price = min(prices)
        max_price = max(prices)
        average_price = sum(prices) / len(prices)

        print(f"Минимальная цена: {min_price}")
        print(f"Максимальная цена: {max_price}")
        print(f"Средняя цена: {average_price}")
    except Exception as e:
        print("Ошибка при анализе цены: ", e)


def cost_analyze(cost):
    """
    Анализирует общую стоимость продуктов и выводит результаты анализа.

    Параметры:
    cost (list): Список стоимостей продуктов.
    """
    try:
        print(f"Общая выручка: {cost}")
    except Exception as e:
        print("Ошибка при стоимости: ", e)


def analyze_data(column_index):
    """
    Анализирует данные в указанном столбце таблицы Google Sheets и выводит результаты анализа
    """

    try:
        data = SHEET.get_all_values()
        data = data[1:]

        prices = []
        quantities = []
        total_cost = []

        for row in data:
            price = float(row[COLUMN_PRICE])
            quantity = int(row[COLUMN_QUANTITIES])
            cost = float(row[COLUMN_COST])

            prices.append(price)
            quantities.append(quantity)
            total_cost.append(cost)

        if column_index == COLUMN_PRICE:
            price_analyze(prices)

        elif column_index == COLUMN_QUANTITIES:
            quantities_analyze(quantities)

        elif column_index == COLUMN_COST:
            cost_analyze(total_cost)

    except Exception as e:
        print("Ошибка при анализе данных: ", e)
