from database import *

initialize_db()


def menu():
    print("\n==============================")
    print(" STUDENT ATTENDANCE SYSTEM ")
    print("==============================")
    print("1. Register Student")
    print("2. View Students")
    print("3. Create Course")
    print("4. View Courses")
    print("5. Enroll Student")
    print("6. Mark Attendance")
    print("7. Attendance History")
    print("8. Attendance Percentage")
    print("9. Low Attendance Report")
    print("10. Course Wise Report")
    print("11. Monthly Summary")
    print("12. Exit")


while True:

    menu()

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        add_student(name, email, phone)

        print("Student Registered Successfully")

    elif choice == "2":

        students = view_students()

        for s in students:
            print(dict(s))

    elif choice == "3":

        course = input("Course Name: ")

        add_course(course)

        print("Course Added Successfully")

    elif choice == "4":

        courses = view_courses()

        for c in courses:
            print(dict(c))

    elif choice == "5":

        sid = int(input("Student ID: "))
        cid = int(input("Course ID: "))

        enroll_student(sid, cid)

        print("Enrollment Successful")

    elif choice == "6":

        sid = int(input("Student ID: "))
        cid = int(input("Course ID: "))
        date = input("Date (YYYY-MM-DD): ")
        status = input("Present/Absent: ")

        mark_attendance(sid, cid, date, status)

        print("Attendance Marked")

    elif choice == "7":

        rows = attendance_history()

        for r in rows:
            print(dict(r))

    elif choice == "8":

        sid = int(input("Student ID: "))

        row = attendance_percentage(sid)

        present = row["present"]
        total = row["total"]

        if total == 0:
            print("No attendance records")
        else:
            percentage = (present * 100) / total
            print(f"Attendance Percentage: {percentage:.2f}%")

    elif choice == "9":

        rows = low_attendance_report()

        for r in rows:
            print(dict(r))

    elif choice == "10":

        rows = course_wise_report()

        for r in rows:
            print(dict(r))

    elif choice == "11":

        rows = monthly_summary()

        for r in rows:
            print(dict(r))

    elif choice == "12":

        print("Thank You")
        break

    else:
        print("Invalid Choice")