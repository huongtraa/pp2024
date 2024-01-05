{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e189e050-732f-4919-95c6-c20a4a256a08",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of students:  2\n",
      "Enter student ID:  02\n",
      "Enter student name:  tra\n",
      "Enter student date of birth:  21/05/2003\n",
      "Enter student ID:  05\n",
      "Enter student name:  hmdx\n",
      "Enter student date of birth:  21/05/2004\n",
      "Enter the number of courses:  1\n",
      "Enter course ID:  7\n",
      "Enter course name:  python\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Available courses:\n",
      "1. python\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select a course (enter the corresponding number):  1\n",
      "Enter mark for student tra:  67\n",
      "Enter mark for student hmdx:  75\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Courses:\n",
      "ID: 7, Name: python\n",
      "Students:\n",
      "ID: 02, Name: tra, DoB: 21/05/2003\n",
      "ID: 05, Name: hmdx, DoB: 21/05/2004\n",
      "Student marks for course python:\n",
      "Student tra: 67.0\n",
      "Student hmdx: 75.0\n"
     ]
    }
   ],
   "source": [
    "def input_number_of_students():\n",
    "    return int(input(\"Enter the number of students: \"))\n",
    "\n",
    "def input_student_information():\n",
    "    student_id = input(\"Enter student ID: \")\n",
    "    student_name = input(\"Enter student name: \")\n",
    "    student_dob = input(\"Enter student date of birth: \")\n",
    "    return {\n",
    "        \"id\": student_id,\n",
    "        \"name\": student_name,\n",
    "        \"dob\": student_dob\n",
    "    }\n",
    "\n",
    "def input_number_of_courses():\n",
    "    return int(input(\"Enter the number of courses: \"))\n",
    "\n",
    "def input_course_information():\n",
    "    course_id = input(\"Enter course ID: \")\n",
    "    course_name = input(\"Enter course name: \")\n",
    "    return {\n",
    "        \"id\": course_id,\n",
    "        \"name\": course_name\n",
    "    }\n",
    "\n",
    "def select_course(courses):\n",
    "    print(\"Available courses:\")\n",
    "    for i, course in enumerate(courses, start=1):\n",
    "        print(f\"{i}. {course['name']}\")\n",
    "    course_index = int(input(\"Select a course (enter the number): \")) - 1\n",
    "    return courses[course_index]\n",
    "\n",
    "def input_student_marks(students):\n",
    "    marks = {}\n",
    "    for student in students:\n",
    "        mark = float(input(f\"Enter mark for student {student['name']}: \"))\n",
    "        marks[student['id']] = mark\n",
    "    return marks\n",
    "\n",
    "def list_courses(courses):\n",
    "    print(\"Courses:\")\n",
    "    for course in courses:\n",
    "        print(f\"ID: {course['id']}, Name: {course['name']}\")\n",
    "\n",
    "def list_students(students):\n",
    "    print(\"Students:\")\n",
    "    for student in students:\n",
    "        print(f\"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}\")\n",
    "\n",
    "def show_student_marks(course, students, marks):\n",
    "    print(f\"Student marks for course {course['name']}:\")\n",
    "    for student in students:\n",
    "        mark = marks.get(student['id'], \"N/A\")\n",
    "        print(f\"Student {student['name']}: {mark}\")\n",
    "\n",
    "def main():\n",
    "    students = []\n",
    "    courses = []\n",
    "    marks = {}\n",
    "    \n",
    "    num_students = input_number_of_students()\n",
    "    for _ in range(num_students):\n",
    "        student = input_student_information()\n",
    "        students.append(student)\n",
    "    \n",
    "    num_courses = input_number_of_courses()\n",
    "    for _ in range(num_courses):\n",
    "        course = input_course_information()\n",
    "        courses.append(course)\n",
    "    \n",
    "    selected_course = select_course(courses)\n",
    "    marks = input_student_marks(students)\n",
    "    \n",
    "    list_courses(courses)\n",
    "    list_students(students)\n",
    "    show_student_marks(selected_course, students, marks)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89e7cb73-09b4-49cb-806c-ab9c10e51c01",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
