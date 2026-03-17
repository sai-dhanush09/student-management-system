from db import get_connection
from tabulate import tabulate

def add_student():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()

    if not name or not age.isdigit():
        print("❌ Invalid input")
        return

    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, int(age), course))
    conn.commit()

    print("✅ Student Added Successfully")
    conn.close()


def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    if data:
        print(tabulate(data, headers=["ID", "Name", "Age", "Course"], tablefmt="fancy_grid"))
    else:
        print("No records found")

    conn.close()


def search_student():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter name to search: ")

    query = "SELECT * FROM students WHERE name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))

    data = cursor.fetchall()

    if data:
        print(tabulate(data, headers=["ID", "Name", "Age", "Course"], tablefmt="fancy_grid"))
    else:
        print("No student found")

    conn.close()


def update_student():
    conn = get_connection()
    cursor = conn.cursor()

    sid = input("Enter Student ID: ")
    new_name = input("Enter new name: ")

    query = "UPDATE students SET name=%s WHERE id=%s"
    cursor.execute(query, (new_name, sid))
    conn.commit()

    print("✅ Updated successfully")
    conn.close()


def delete_student():
    conn = get_connection()
    cursor = conn.cursor()

    sid = input("Enter Student ID: ")

    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (sid,))
    conn.commit()

    print("❌ Deleted successfully")
    conn.close()