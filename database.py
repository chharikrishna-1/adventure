import sqlite3
import os

DB_PATH = "data/attendance.db"

def get_connection():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    return conn


def initialize_db():
    conn = get_connection()

    with open("schema.sql", "r") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()


# ---------------- STUDENTS ---------------- #

def add_student(name, email, phone):
    conn = get_connection()

    conn.execute(
        "INSERT INTO students(name,email,phone) VALUES(?,?,?)",
        (name, email, phone)
    )

    conn.commit()
    conn.close()


def view_students():
    conn = get_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return students


# ---------------- COURSES ---------------- #

def add_course(course_name):
    conn = get_connection()

    conn.execute(
        "INSERT INTO courses(course_name) VALUES(?)",
        (course_name,)
    )

    conn.commit()
    conn.close()


def view_courses():
    conn = get_connection()

    courses = conn.execute(
        "SELECT * FROM courses"
    ).fetchall()

    conn.close()

    return courses


# ---------------- ENROLLMENT ---------------- #

def enroll_student(student_id, course_id):
    conn = get_connection()

    conn.execute(
        "INSERT INTO enrollments(student_id,course_id) VALUES(?,?)",
        (student_id, course_id)
    )

    conn.commit()
    conn.close()


# ---------------- ATTENDANCE ---------------- #

def mark_attendance(student_id, course_id, date, status):
    conn = get_connection()

    conn.execute("""
        INSERT INTO attendance
        (student_id,course_id,attendance_date,status)
        VALUES(?,?,?,?)
    """, (student_id, course_id, date, status))

    conn.commit()
    conn.close()


def attendance_history():
    conn = get_connection()

    rows = conn.execute("""
        SELECT s.name,
               c.course_name,
               a.attendance_date,
               a.status
        FROM attendance a
        INNER JOIN students s
        ON a.student_id=s.student_id
        INNER JOIN courses c
        ON a.course_id=c.course_id
        ORDER BY a.attendance_date
    """).fetchall()

    conn.close()

    return rows


# ---------------- REPORTS ---------------- #

def attendance_percentage(student_id):
    conn = get_connection()

    row = conn.execute("""
        SELECT
        COUNT(CASE WHEN status='Present' THEN 1 END) AS present,
        COUNT(*) AS total
        FROM attendance
        WHERE student_id=?
    """, (student_id,)).fetchone()

    conn.close()

    return row


def low_attendance_report():
    conn = get_connection()

    rows = conn.execute("""
        SELECT
        s.student_id,
        s.name,
        ROUND(
        COUNT(CASE WHEN a.status='P' or a.status='Present' THEN 1 END)
        *100.0/COUNT(*),2
        ) AS percentage
        FROM attendance a
        JOIN students s
        ON a.student_id=s.student_id
        GROUP BY s.student_id,s.name
        HAVING percentage < 75
    """).fetchall()

    conn.close()

    return rows


def course_wise_report():
    conn = get_connection()

    rows = conn.execute("""
        SELECT
        c.course_name,
        COUNT(CASE WHEN a.status='Present' or status='P' THEN 1 END) AS Present,
        COUNT(CASE WHEN a.status='Absent' or status='A' THEN 1 END) AS Absent
        FROM attendance a
        JOIN courses c
        ON a.course_id=c.course_id
        GROUP BY c.course_name
    """).fetchall()

    conn.close()

    return rows


def monthly_summary():
    conn = get_connection()

    rows = conn.execute("""
        SELECT
        substr(attendance_date,1,7) AS Month,
        COUNT(*) AS Total,
        COUNT(CASE WHEN status='Present' or status='P' THEN 1 END) AS Present,
        COUNT(CASE WHEN status='Absent' or status='A' THEN 1 END) AS Absent
        FROM attendance
        GROUP BY Month
    """).fetchall()

    conn.close()

    return rows