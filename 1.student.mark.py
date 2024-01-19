def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return {
        "id": student_id,
        "name": student_name,
        "dob": student_dob
    }

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {
        "id": course_id,
        "name": course_name
    }

def select_course(courses):
    print("Available courses:")
    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course['name']}")
    course_index = int(input("Select a course (enter the number): ")) - 1
    return courses[course_index]

def input_student_marks(students):
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']}: "))
        marks[student['id']] = mark
    return marks

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_student_marks(course, students, marks):
    print(f"Student marks for course {course['name']}:")
    for student in students:
        mark = marks.get(student['id'], "N/A")
        print(f"Student {student['name']}: {mark}")

def main():
    students = []
    courses = []
    marks = {}
    
    num_students = input_number_of_students()
    for _ in range(num_students):
        student = input_student_information()
        students.append(student)
    
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course = input_course_information()
        courses.append(course)
    
    selected_course = select_course(courses)
    marks = input_student_marks(students)
    
    list_courses(courses)
    list_students(students)
    show_student_marks(selected_course, students, marks)

if __name__ == "__main__":
    main()
