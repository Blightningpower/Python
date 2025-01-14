import unittest
from testApplicatie import Student, Group, ClassManager


class TestClassManager(unittest.TestCase):
    def test_maximum_groups(self):
        """Test dat het niet mogelijk is om meer dan 12 groepen toe te voegen."""
        manager = ClassManager()

        # Voeg 12 groepen toe
        for i in range(12):
            manager.addGroup(Group(f"Group {i+1}"))

        self.assertEqual(len(manager.groups), 12)

        # Probeer een 13e groep toe te voegen
        manager.addGroup(Group("Group 13"))
        self.assertEqual(len(manager.groups), 12)  # Nog steeds 12 groepen


    def test_schedulable_group(self):
        """Test dat een groep inplanbaar is als er 6-8 studenten in zitten."""
        group = Group("TestGroup")

        # Voeg 5 studenten toe (ondergrens niet bereikt)
        for i in range(5):
            group.addStudent(Student(100000 + i, f"Student {i+1}"))
        self.assertIn("* Groep is nog niet inplanbaar", str(group))

        # Voeg 1 extra student toe (totaal 6, precies inplanbaar)
        group.addStudent(Student(100005, "Student 6"))
        self.assertNotIn("* Groep is nog niet inplanbaar", str(group))

        # Voeg 2 extra studenten toe (totaal 8, nog steeds inplanbaar)
        group.addStudent(Student(100006, "Student 7"))
        group.addStudent(Student(100007, "Student 8"))
        self.assertNotIn("* Groep is nog niet inplanbaar", str(group))

        # Voeg een extra student toe (meer dan 8, niet meer inplanbaar)
        group.addStudent(Student(100008, "Student 9"))
        self.assertIn("* Groep is nog niet inplanbaar", str(group))


    def test_valid_student_number(self):
        """Test dat een studentnummer een getal van 6 cijfers is."""
        # Correct studentnummer
        student_valid = Student(123456, "Valid Student")
        self.assertEqual(len(str(student_valid.studentNumber)), 6)

        # Incorrect studentnummer
        student_invalid = Student(12345, "Invalid Student")
        self.assertNotEqual(len(str(student_invalid.studentNumber)), 6)
        

    def test_unique_group_code(self):
        """Test dat een groep alleen wordt toegevoegd als de groepscode uniek is."""
        manager = ClassManager()

        # Voeg een groep toe
        group_a = Group("A")
        manager.addGroup(group_a)

        # Probeer een duplicaat toe te voegen
        group_duplicate = Group("A")
        manager.addGroup(group_duplicate)

        # Controleer dat er maar één groep met code "A" is
        group_codes = [group.code for group in manager.groups]
        self.assertEqual(len(group_codes), 1)
        self.assertIn("A", group_codes)  # Controleer dat "A" aanwezig is


if __name__ == "__main__":
    unittest.main()