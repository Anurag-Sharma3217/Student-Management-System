def save_data(students):

    if len(students) > 0:
        file = open("students.txt", "w")
        for student in students:
            file.write(student.name + "," + str(student.marks) + "\n")
        file.close()
        print("Data saved.")

    else:
        print("List is empty.")

def load_data(students, pupils):
    students.clear()
    file = open("students.txt", "r")
    for line in file:
        parts = line.strip().split(",")
        name = parts[0]
        marks = int(parts[1])
        student = pupils(name, marks)
        students.append(student)
    file.close()
    print("Data loaded.")
    
