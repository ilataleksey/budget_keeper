import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        initial_amount REAL DEFAULT 0,
        current_amount REAL DEFAULT 0
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        is_income BOOLEAN DEFAULT 0  # 0=расход, 1=доход
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        budget_id INTEGER REFERENCES budgets(id),
        category_id INTEGER REFERENCES categories(id),
        amount REAL NOT NULL,
        description TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_income BOOLEAN DEFAULT 0
    )
    ''')

    # Стандартные категории
    cursor.executemany(
        'INSERT OR IGNORE INTO categories (name, is_income) VALUES (?, ?)',
        [
            ('Еда', 0),
            ('Транспорт', 0),
            ('Зарплата', 0),
            ('Дом', 0),
            ('Здоровье', 0),
            ('Инвестиции', 0),
            ('Корректировка', 0),
            ('Красота', 0),
            ('Кредит', 0),
            ('Налоги', 0),
            ('Одежда', 0),
            ('Отпуск', 0),
            ('Подарки', 0),
            ('Работа', 0),
            ('Развлечения', 0),
            ('Эм', 0),
        ]
    )
    conn.commit()
    conn.close()