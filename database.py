import sqlite3
connection = sqlite3.connect("data.db")


def create_table():
    connection.execute(
        "CREATE TABLE IF NOT EXISTS entries (id INTEGER, name TEXT, dateDelivery TEXT, time TEXT, paymentMode TEXT, contactNum TEXT)")
    connection.commit()


def close_database():
    connection.close()


def add_entry(entry_id, entry_name, entry_dateDelivery, entry_time, entry_paymentMode, entry_contactNum):
    connection.execute(
        f"INSERT INTO entries VALUES ({entry_id}, '{entry_name}', '{entry_dateDelivery}', '{entry_time}', '{entry_paymentMode}', '{entry_contactNum}');")
    connection.commit()


def get_entries():
    return connection.execute("SELECT * FROM entries;")

def del_entry(id_for_deletion):
    connection.execute(f"DELETE FROM entries WHERE id={id_for_deletion};")
    connection.commit()