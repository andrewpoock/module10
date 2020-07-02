import unittest
from class_definitions import student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = student.Student('Brown', 'John', 'Liberal Arts', 3.8)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Brown')
        self.assertEqual(self.student.first_name, 'John')
        self.assertEqual(self.student.major, 'Liberal Arts')

    def test_object_created_all_attributes(self):
        student1 = student.Student('Brown', 'John', 'Liberal Arts', 3.8)
        assert student1.last_name == 'Brown'
        assert student1.first_name == 'John'
        assert student1.major == 'Liberal Arts'
        assert student1.gpa == 3.8

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Brown, John has major Liberal Arts with gpa: 3.8')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = student.Student('123', 'John', 'Liberal Arts')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = student.Student('Brown', '123', 'Liberal Arts')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = student.Student('Brown', 'John', '123')

    def test_person_class_display_name_ssn(self):
        with self.assertRaises(ValueError):
            p = student.Student('Brown', 'John', 'Liberal Arts', 'jjj')


if __name__ == '__main__':
    unittest.main()
