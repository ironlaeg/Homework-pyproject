class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()


def average_hw_grade_for_course(students, course):
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])
    if not grades:
        return 0
    return round(sum(grades) / len(grades), 1)


def average_lecture_grade_for_course(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    if not grades:
        return 0
    return round(sum(grades) / len(grades), 1)


good_student = Student('Vova', 'Farniev', 'male')
good_student.courses_in_progress += ['Python', 'Web-Python']
dumb_student = Student('Biba', 'Bobovna', 'female')
dumb_student.courses_in_progress += ['Python', 'Web-Python']


smart_lecturer = Lecturer('Nina', 'Pavlovna')
smart_lecturer.courses_attached += ['Python']
smart_lecturer.grades['Python'] = [9, 8]
smartest_lecturer = Lecturer('Anna', 'Ushakova')
smartest_lecturer.courses_attached += ['Web-Python']
smartest_lecturer.grades['Web-Python'] = [10, 10]


cool_reviewer = Reviewer('Bogdan', 'Suleimanov')
cool_reviewer.courses_attached += ['Python']
hot_reviewer = Reviewer('Alexis', 'Fawx')
hot_reviewer.courses_attached += ['Web-Python']

cool_reviewer.rate_hw(good_student, 'Python', 10)
cool_reviewer.rate_hw(dumb_student, 'Python', 2)
hot_reviewer.rate_hw(good_student, 'Web-Python', 6)
hot_reviewer.rate_hw(dumb_student, 'Web-Python', 10)


print(good_student)
print(dumb_student)
print(smart_lecturer)
print(smartest_lecturer)
print(cool_reviewer)
print(hot_reviewer)


print(good_student > dumb_student)
print(good_student == dumb_student)

print(smart_lecturer < smartest_lecturer)
print(smart_lecturer == smartest_lecturer)

students_list = [good_student, dumb_student]
print(f"Средняя оценка за домашние задания по курсу Python: {average_hw_grade_for_course(students_list, 'Python')}")


lecturers_list = [smart_lecturer, smartest_lecturer]
print(f"Средняя оценка за лекции по курсу Web-Python: {average_lecture_grade_for_course(lecturers_list, 'Web-Python')}")