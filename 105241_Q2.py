# Online Course Management System
# 105241_Q2.py
# Class: Student and Instructor Management System

class Student:
    def __init__(self, name, student_id):
        # Initialize student with name, ID, and empty assignments dictionary
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Format: {assignment_name: grade}

    def add_assignment(self, assignment_name, grade):
        """Add or update an assignment with its grade"""
        self.assignments[assignment_name] = grade
        print(f"Added grade '{grade}' for assignment '{assignment_name}' to {self.name}'s record")

    def display_grades(self):
        """Display all grades for the student"""
        print(f"\nGrades for {self.name} (ID: {self.student_id}):")
        if not self.assignments:
            print("No assignments recorded")
            return

        for assignment, grade in self.assignments.items():
            print(f"- {assignment}: {grade}")


def assign_grade(student, assignment_name, grade):
    """Assign a grade to a student's assignment"""
    student.add_assignment(assignment_name, grade)


class Instructor:
    def __init__(self, name, course_name):
        # Initialize instructor with name, course, and empty students list
        self.name = name
        self.course_name = course_name
        self.students = []  # List of Student objects

    def add_student(self, student):
        """Add a student to the course"""
        self.students.append(student)
        print(f"Added student: {student.name} (ID: {student.student_id})")

    def display_students(self):
        """Display all students and their grades"""
        print(f"\nStudents in {self.course_name} (Instructor: {self.name}):")
        if not self.students:
            print("No students enrolled")
            return

        for student in self.students:
            student.display_grades()

# Main function to run the online course management system
def main():
    # Initialize instructor
    print("=== Online Course Management System ===")
    instructor_name = input("Enter instructor name: ")
    course_name = input("Enter course name: ")
    instructor = Instructor(instructor_name, course_name)

    while True:
        print("\n=== Instructor Menu ===")
        print("1. Add a student")
        print("2. Assign a grade to a student")
        print("3. Display all students and their grades")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Add a new student
            print("\n=== Add Student ===")
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            new_student = Student(name, student_id)
            instructor.add_student(new_student)

        elif choice == '2':
            # Assign grade to a student
            print("\n=== Assign Grade ===")
            if not instructor.students:
                print("No students available")
                continue

            # List students
            print("Select a student:")
            for i, student in enumerate(instructor.students, 1):
                print(f"{i}. {student.name} (ID: {student.student_id})")

            try:
                student_idx = int(input("Enter student number: ")) - 1
                if 0 <= student_idx < len(instructor.students):
                    assignment = input("Enter assignment name: ")
                    grade = input("Enter grade: ")
                    assign_grade(
                        instructor.students[student_idx],
                        assignment,
                        grade
                    )
                else:
                    print("Invalid student number")
            except ValueError:
                print("Please enter a valid number")

        elif choice == '3':
            # Display all students and their grades
            print("\n=== Student Grades ===")
            instructor.display_students()

        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Main entry point for the program
if __name__ == "__main__":
    main() # This line ensures the main function runs when the script is executed
# End Script