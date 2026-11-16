"""Калькулятор личных финансов: доходы, расходы, баланс."""

import os

PINK = "\033[95m"
RESET = "\033[0m"

# Список операций: словари с ключами type, amount, category, date
operations = []


def read_amount():
    while True:
        raw = input("Сумма: ").strip().replace(",", ".")
        try:
            amount = float(raw)
        except ValueError:
            print("Введите число, например 1500 или 99.90")
            continue
        if amount <= 0:
            print("Сумма должна быть больше нуля")
            continue
        return amount


def read_date():
    # Формат ДД.ММ.ГГГГ, проверяем без библиотек
    while True:
        raw = input("Дата (ДД.ММ.ГГГГ): ").strip()
        parts = raw.split(".")
        if len(parts) == 3 and all(p.isdigit() for p in parts):
            day, month, year = (int(p) for p in parts)
            if 1 <= day <= 31 and 1 <= month <= 12 and len(parts[2]) == 4:
                return raw
        print("Неверная дата, пример: 16.11.2026")


def add_operation(kind):
    amount = read_amount()
    category = input("Категория: ").strip() or "Без категории"
    date = read_date()
    operations.append({"type": kind, "amount": amount, "category": category, "date": date})
    print("Операция добавлена")


def show_operations():
    if not operations:
        print("Операций пока нет")
        return
    for i, op in enumerate(operations, 1):
        sign = "+" if op["type"] == "income" else "-"
        print(f"{i}. {op['date']}  {sign}{op['amount']:.2f}  {op['category']}")


def get_balance():
    income = sum(op["amount"] for op in operations if op["type"] == "income")
    expense = sum(op["amount"] for op in operations if op["type"] == "expense")
    return income, expense, income - expense


def show_balance():
    income, expense, balance = get_balance()
    print(f"Доходы:  {income:.2f}")
    print(f"Расходы: {expense:.2f}")
    print(f"Баланс:  {balance:.2f}")


def main():
    os.system("")  # включает цвета ANSI в консоли Windows
    print(PINK, end="")
    actions = {
        "1": lambda: add_operation("income"),
        "2": lambda: add_operation("expense"),
        "3": show_operations,
        "4": show_balance,
    }
    try:
        while True:
            print("\n=== Калькулятор личных финансов ===")
            print("1. Добавить доход")
            print("2. Добавить расход")
            print("3. Список операций")
            print("4. Баланс")
            print("0. Выход")
            choice = input("Выберите пункт: ").strip()
            if choice == "0":
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Нет такого пункта")
    except (KeyboardInterrupt, EOFError):
        print()
    finally:
        print("До свидания!" + RESET)


if __name__ == "__main__":
    main()
