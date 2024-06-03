import sqlite3

connection = sqlite3.connect('students.db')


cursor = connection.cursor()

cursor.execute('CREATE TABLE Students(id INTEGER PRIMARY KEY, name STR, age INT)')
cursor.execute('CREATE TABLE Grades(id INTEGER PRIMARY KEY, student_id, subject STR, grade FLOAT)')

class University:
    def __init__(self, name):
        self.name = name
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()

    def add_student(self, name, age):
        self.cursor.execute('INSERT INTO Students(name, age) VALUES (?, ?)', (name, age))
        self.connection.commit()

    def add_grade(self, student_id, subject, grade):
        self.cursor.execute('INSERT INTO Grades(student_id, subject, grade) VALUES(?, ?, ?)',
                            (student_id, subject, grade))
        self.connection.commit()

    def get_students(self, subject=None):
        if subject:
            self.cursor.execute(f"SELECT students.name, students.age, grades.subject, grades.grade FROM Students "
                                f"JOIN Grades ON student_id = grades.student_id WHERE grades.subject = '{subject}'")

        else:
            self.cursor.execute('SELECT students.name, students.age, grades.subject, '
                                'grades.grade FROM Students JOIN Grades ON student_id = grades.student_id')
            self.connection.commit()

        student_data = self.cursor.fetchall()
        self.connection.commit()

        for i in student_data:
            if student_data:
                return student_data
            print(student_data)
            print(i)

            self.connection.commit()
            cursor.close()

    def __del__(self):
        self.connection.close()

university = University('Urban')
university.add_student('Boris', 20)
university.add_student('Vitaliy', 21)
university.add_student('Ira', 23)
university.add_student('Vera', 24)

university.add_grade(1, 'SQL', 2)
university.add_grade(2, 'SQL', 2)
university.add_grade(3, 'SQL', 2)
university.add_grade(4, 'SQL', 2)

print(university.get_students())
print(university.get_students('SQL'))

