import sqlite3

# Create database connection
def get_connection():
    return sqlite3.connect("donors.db")


# Create donors table
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            blood_group TEXT NOT NULL,
            phone TEXT NOT NULL,
            city TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Insert donor information
def add_donor(name, age, gender, blood_group, phone, city, address):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO donors
        (name, age, gender, blood_group, phone, city, address)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, age, gender, blood_group, phone, city, address))

    conn.commit()
    conn.close()


# Get all registered donors
def get_all_donors():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, age, gender, blood_group, phone, city
        FROM donors
        ORDER BY id DESC
    """)

    donors = cursor.fetchall()

    conn.close()

    return donors


# Get one donor by ID
def get_donor_by_id(donor_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM donors WHERE id = ?",
        (donor_id,)
    )

    donor = cursor.fetchone()
    conn.close()

    return donor


# Update donor details
def update_donor(donor_id, name, age, gender,
                 blood_group, phone, city, address):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE donors
        SET name = ?, age = ?, gender = ?,
            blood_group = ?, phone = ?, city = ?, address = ?
        WHERE id = ?
    """, (name, age, gender, blood_group,
          phone, city, address, donor_id))

    conn.commit()
    conn.close()


# Delete donor
def delete_donor(donor_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM donors WHERE id = ?",
        (donor_id,)
    )

    conn.commit()
    conn.close()
