import sqlite3
connection = sqlite3.connect("data.db")


def create_table():
    connection.execute(
        "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT)")
    connection.commit()


def close_database():
    connection.close()


def add_entry(entry_content, entry_date):
    connection.execute(
        f"INSERT INTO entries VALUES ('{entry_content}', '{entry_date}');")
    connection.commit()


def get_entries():
    return connection.execute("SELECT * FROM entries;")
