class Student:
    def __init__(self, studentNumber, name):
        self.studentNumber = studentNumber
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.studentNumber})"


class Group:
    def __init__(self, code):
        self.code = code
        self.students = set()  # Gebruik een set in plaats van een lijst

    def getStudentList(self):
        return [str(student) for student in self.students]

    def addStudent(self, student):
        if len(self.students) >= 8:  # Hard limit op 8 studenten
            print(f"* Kan student {student.name} ({student.studentNumber}) niet toevoegen. Groep {self.code} zit vol.")
        elif student in self.students:  # Controleer of de student al aanwezig is
            print(f"* Student {student.name} ({student.studentNumber}) is al toegevoegd aan groep {self.code}.")
        else:
            self.students.add(student)

    def removeStudent(self, studentNumber):
        for student in self.students:
            if student.studentNumber == studentNumber:
                self.students.remove(student)
                print(f"Student {student.name} is verwijderd uit groep {self.code}.")
                return
        print(f"Student met nummer {studentNumber} niet gevonden in groep {self.code}.")

    def __str__(self):
        status = "* Groep is nog niet inplanbaar" if not (6 <= len(self.students) <= 8) else ""
        student_list = "\n".join(self.getStudentList())
        return f"Indeling groep {self.code}\n{status}\n{student_list}"


class ClassManager:
    def __init__(self):
        self.groups = []  # Gebruik een lijst

    def addGroup(self, group):
        if len(self.groups) >= 12:
            print("* Kan geen nieuwe groep toevoegen. Maximum aantal groepen bereikt.")
            return

        # Controleer op unieke groepscode
        if any(existing_group.code == group.code for existing_group in self.groups):
            print(f"* Groep met code {group.code} bestaat al en wordt niet toegevoegd.")
            return

        self.groups.append(group)


# Testcode
if __name__ == "__main__":
    # Studenten aanmaken
    students = [
        Student(1234, "Luc"),
        Student(4534, "Joost"),
        Student(4536, "Maarten"),
        Student(1234, "Joost"),
        Student(2345, "Maarten"),
        Student(3456, "Fatima"),
        Student(4567, "Mirjam"),
        Student(5678, "Donald"),
        Student(6789, "Jahmal"),
    ]

    # Groepen aanmaken
    group_a = Group("A", max_capacity=4)
    group_e = Group("E", max_capacity=6)

    # Studenten toevoegen
    group_a.addStudent(students[0])
    group_a.addStudent(students[1])
    group_a.addStudent(students[2])  # Te veel studenten

    group_e.addStudent(students[3])
    group_e.addStudent(students[4])
    group_e.addStudent(students[5])
    group_e.addStudent(students[6])
    group_e.addStudent(students[7])
    group_e.addStudent(students[8])

    # ClassManager aanmaken
    manager = ClassManager()
    manager.addGroup(group_a)
    manager.addGroup(group_e)

    # Rooster tonen
    manager.printSchedule()