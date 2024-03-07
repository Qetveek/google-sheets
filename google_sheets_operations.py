from google_sheets_functions import (
    append_data,
    edit_row,
    up_user_data,
    find_rows_by_criteria,
    find_rows_by_partial_match,
    edit_row_by_number,
    analyze_data,
    is_found_rows,
    get_user_choice,
)
from google_sheets_crud import (
    append_data,
    update_cell,
    delete_row,
    update_row_numbers,
    read_data,
)
from config import COLUMN_COST, COLUMN_PRICE, COLUMN_QUANTITIES


def test_new_data_row():
    print("starting test!")

    new_data_row = ["Продано", "Возврат"]

    append_data(new_data_row)
    print("done!")


def test_update_cell():
    print("starting test!")
    update_cell(2, 4, "500")
    print("done!")


def test_row_numbers():
    print("starting test!")
    update_row_numbers()
    print("done!")


def test_edit_rows():
    print("starting test!")

    row_number_to_edit = 10
    product_name = "Название продукта"
    price = 100
    quantity = 100

    edit_row(row_number_to_edit, product_name, price, quantity)
    print("done!")


def test_up_user_data():
    print("starting test!")
    up_user_data()
    print("done!")


def test_delete_row():
    print("starting test!")

    row_to_delete = 12

    delete_row(row_to_delete)
    print("done!")


def test_find_rows_by_criteria():
    print("starting test!")

    search_column_index = 1
    search_value = "Кукла"
    found_rows = find_rows_by_criteria(search_column_index, search_value)

    if found_rows:
        print("\nНайденные строки:")
        for row in found_rows:
            print(row)
    else:
        print("\nСтроки с указанным критерием не найдены.")

    print("done!")


def test_find_rows_by_partial_match():
    print("starting test!")

    search_column_index = 1
    keyword = "Кукла"
    found_rows = find_rows_by_partial_match(search_column_index, keyword)

    if is_found_rows(found_rows):
        row_number_to_edit = get_user_choice(found_rows)
        if row_number_to_edit:
            edit_row_by_number(search_column_index, keyword, row_number_to_edit)

    print("done!")


def test_analyze_data():
    print("starting test!")

    print("Выберите столбец для анализа данных:")
    print(f"1. Цена")
    print(f"2. Количество")
    print(f"3. Стоимость")

    choice = int(input("Введите номер столбца для анализа данных: "))

    if choice < 1 or choice > 3:
        print("Ошибка: Некорректный номер столбца.")
        return

    if choice == 1:
        choice = COLUMN_PRICE
    elif choice == 2:
        choice = COLUMN_QUANTITIES
    elif choice == 3:
        choice = COLUMN_COST

    analyze_data(choice)

    print("done!")


def test_update_row_numbers():
    print("starting test!")
    update_row_numbers()
    print("done!")


def main():
    read_data()


if __name__ == "__main__":
    main()
