import sqlite3

# Подключение к базе данных (если база данных не существует, она будет создана)
conn = sqlite3.connect('example2.db')
cursor = conn.cursor()

# Создание таблицы items
cursor.execute('''
    CREATE TABLE items (
        key TEXT PRIMARY KEY,
        name TEXT
    )
''')

# Создание таблицы operations
cursor.execute('''
    CREATE TABLE operations (
        equipment_id INTEGER,
        description TEXT
    )
''')

# Создание таблицы equipment
cursor.execute('''
    CREATE TABLE equipment (
        id TEXT PRIMARY KEY,
        name TEXT
    )
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
