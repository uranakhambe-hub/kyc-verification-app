import sqlite3

def init_db():
    conn = sqlite3.connect("kyc.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kyc_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        dob TEXT,
        address TEXT,
        id_number TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_record(data):
    conn = sqlite3.connect("kyc.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO kyc_records (name, dob, address, id_number)
    VALUES (?, ?, ?, ?)
    """, (data["name"], data["dob"], data["address"], data["id_number"]))

    conn.commit()
    conn.close()