def get_name(message):

    while True:
        
        name = input(message)
        if name.replace(" ", "").isalpha():
            break
        print("Enter letter only.")

    return name
    

def get_number(message):

    while True:
        try:
            return int(input(message))
            break
        except ValueError:
            print("Enter numbers only.")


def find_student(students, name):
    for student in students:
        if student.name.lower() == name.lower():
            return student

    return None

