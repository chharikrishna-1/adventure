# Student Attendance Management System

## Problem Statement

Schools, colleges, and training institutes need an efficient way to track student attendance, monitor participation, and generate attendance reports. Manual attendance management is time-consuming and prone to errors. This project automates attendance tracking using Python and SQLite.

---

## Features

* Student Registration
* Course Creation
* Student Enrollment
* Daily Attendance Marking
* Attendance History
* Attendance Percentage Calculation
* Students Below 75% Attendance Report
* Course-wise Attendance Report
* Monthly Attendance Summary
* Menu-Driven Interface

---

## Technologies Used

* Python 3
* SQLite
* SQL
* Git
* GitHub

---

## Database Tables

### Students

Stores student information.

| Column     | Type         |
| ---------- | ------------ |
| student_id | INTEGER (PK) |
| name       | TEXT         |
| email      | TEXT         |
| phone      | TEXT         |

### Courses

Stores course information.

| Column      | Type         |
| ----------- | ------------ |
| course_id   | INTEGER (PK) |
| course_name | TEXT         |

### Enrollments

Stores student-course enrollments.

| Column        | Type         |
| ------------- | ------------ |
| enrollment_id | INTEGER (PK) |
| student_id    | INTEGER (FK) |
| course_id     | INTEGER (FK) |

### Attendance

Stores attendance records.

| Column          | Type         |
| --------------- | ------------ |
| attendance_id   | INTEGER (PK) |
| student_id      | INTEGER (FK) |
| course_id       | INTEGER (FK) |
| attendance_date | TEXT         |
| status          | TEXT         |

---

## SQL Concepts Used

* INSERT
* SELECT
* UPDATE
* DELETE
* INNER JOIN
* COUNT()
* GROUP BY
* Aggregate Functions
* Foreign Keys

---

## Project Structure

```text
student-attendance-system/
│
├── main.py
├── database.py
├── schema.sql
├── requirements.txt
├── README.md
├── data/
└── screenshots/
```

---

## Reports Generated

### Attendance Percentage Report

Calculates attendance percentage for individual students.

### Low Attendance Report

Displays students whose attendance percentage is below 75%.

### Course-wise Attendance Report

Shows present and absent counts for each course.

### Monthly Attendance Summary

Provides monthly attendance statistics.

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/chharikrishna-1/adventure.git
```

### Navigate to Project Folder

```bash
cd adventure
```

### Run the Application

```bash
python main.py
```

---

## Sample Menu

```text
==============================
 STUDENT ATTENDANCE SYSTEM
==============================
1. Register Student
2. View Students
3. Create Course
4. View Courses
5. Enroll Student
6. Mark Attendance
7. Attendance History
8. Attendance Percentage
9. Low Attendance Report
10. Course Wise Report
11. Monthly Summary
12. Exit
```

---

## Future Enhancements

* Login Authentication
* Export Reports to CSV
* Student Search Functionality
* Attendance Dashboard
* Graphical User Interface (GUI)

---

## Author

Hari Krishna
