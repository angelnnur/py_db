import sqlite3

# создаем соединение с нашей базой данных
conn = sqlite3.connect("client.sqlite")
cursor = conn.cursor()

# Запрос для копирования причин простоя с имеющихся станков
# Фрезер №3
cursor.execute(
    "INSERT INTO endpoint_reasons (endpoint_id, reason_name, reason_hierarchy) SELECT ?, reason_name, reason_hierarchy FROM endpoint_reasons WHERE endpoint_id = (SELECT id FROM endpoints WHERE name = ?)",
    (9, "Фрезерный станок"),
)
# Пильный аппарат №2
cursor.execute(
    "INSERT INTO endpoint_reasons (endpoint_id, reason_name, reason_hierarchy) SELECT ?, reason_name, reason_hierarchy FROM endpoint_reasons WHERE endpoint_id = (SELECT id FROM endpoints WHERE name = ?)",
    (8, "Старый ЧПУ"),
)
# Сварочный аппарат №1
cursor.execute(
    "INSERT INTO endpoint_reasons (endpoint_id, reason_name, reason_hierarchy) SELECT ?, reason_name, reason_hierarchy FROM endpoint_reasons WHERE endpoint_id = (SELECT id FROM endpoints WHERE name = ?)",
    (7, "Сварка"),
)

conn.commit()
