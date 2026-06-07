students = []

def add_student(students_list, name, roll, marks=[]):
    new_student = {
        "name": name,
        "roll": roll,
        "marks": marks.copy()
    }
    students_list.append(new_student)
    print(f"Student {name} added successfully!")

def calculate_stats(marks):
    if not marks:
        return {"average": 0, "highest": 0, "lowest": 0, "grade": "N/A"}
    
    average = sum(marks)/len(marks)
    grade = assign_grade(average)
    
    return {
        "average": average,
        "highest": max(marks),
        "lowest": min(marks),
        "grade": grade
    }

def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def display_all_students(students_list):
    if not students_list:
        print("No students in the system")
        return
    print("\n{:<10} {:<15} {:<20} {:<10} {:<10} {:<10} {:<6}".format(
        "Roll No.", "Name", "Marks", "Average", "Highest", "Lowest", "Grade"
    ))
    print("-"*85)
    for student in students_list:
        stats = calculate_stats(student["marks"])
        print("{:<10} {:<15} {:<20} {:<10.2f} {:<10} {:<10} {:<6}".format(
            student["roll"],
            student["name"],
            str(student["marks"]),
            stats["average"],
            stats["highest"],
            stats["lowest"],
            stats["grade"]
        ))

def display_best_per_subject(students_list):
    if not students_list or not students_list[0]["marks"]:
        print("Not enough data to determine best per subject.")
        return

    num_subjects = len(students_list[0]["marks"])
    best_marks = [0] * num_subjects

    for student in students_list:
        for i in range(num_subjects):
            if i < len(student["marks"]):
                best_marks[i] = max(best_marks[i], student["marks"][i])

    print("\n🏆 Best Marks Per Subject:")
    for i, mark in enumerate(best_marks, start=1):
        print(f"Subject {i}: {mark}")

# important h change ni krna h isse neeche ka 
if __name__ == "__main__":
    n = int(input("Enter number of students: "))
    
    for _ in range(n):
        name = input("Enter name of student: ")
        roll = int(input("Enter roll number: "))
        marks_input = input("Enter marks separated by space: ")
        marks = list(map(int, marks_input.strip().split())) if marks_input.strip() else []
        
        add_student(students, name, roll, marks)

    print("\n📋 Final student list with stats:")
    display_all_students(students)

    display_best_per_subject(students)
def display_best_per_subject(students_list):
    if not students_list or not students_list[0]["marks"]:
        print("Not enough data to determine best per subject.")
        return

    num_subjects = len(students_list[0]["marks"])
    best_marks = [0] * num_subjects
    best_students = [""] * num_subjects
 
    for student in students_list:
        for i in range(num_subjects):
            if i < len(student["marks"]) and student["marks"][i] >= best_marks[i]:
                best_marks[i] = student["marks"][i]
                best_students[i] = student["name"]

    print("\n🏆 Best Marks Per Subject:")
    for i in range(num_subjects):
        print(f"Subject {i+1}: {best_marks[i]} ({best_students[i]})")