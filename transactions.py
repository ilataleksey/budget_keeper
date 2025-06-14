# transactions.py
from datetime import datetime


def add_transaction(budget_id, category_id, amount, description, is_income=False):
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()

    # 1. Добавляем транзакцию
    cursor.execute('''
    INSERT INTO transactions 
    (budget_id, category_id, amount, description, is_income)
    VALUES (?, ?, ?, ?, ?)
    ''', (budget_id, category_id, amount, description, is_income))

    # 2. Обновляем бюджет
    sign = 1 if is_income else -1
    cursor.execute('''
    UPDATE budgets 
    SET current_amount = current_amount + ?
    WHERE id = ?
    ''', (sign * amount, budget_id))

    conn.commit()
    conn.close()