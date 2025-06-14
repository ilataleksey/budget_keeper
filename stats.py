# stats.py
def get_stats_by_period(start_date, end_date):
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT 
        strftime('%Y-%m', date) as month,
        SUM(CASE WHEN is_income THEN amount ELSE 0 END) as income,
        SUM(CASE WHEN NOT is_income THEN amount ELSE 0 END) as expense
    FROM transactions
    WHERE date BETWEEN ? AND ?
    GROUP BY month
    ''', (start_date, end_date))

    return cursor.fetchall()


def get_stats_by_category():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT c.name, SUM(t.amount) 
    FROM transactions t
    JOIN categories c ON t.category_id = c.id
    GROUP BY c.name
    ''')
    return cursor.fetchall()