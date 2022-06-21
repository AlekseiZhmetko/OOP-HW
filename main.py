students = []
lecturers = []

def avg_overall_grade(dict): # функция для определения средней оценки по словарю
    all_grades = []
    for i in dict.values():
        list_avg = sum(i) / len(i)
        all_grades.append(list_avg)
    avg_overall_grade = sum(all_grades) / len(all_grades)
    return "%.1f" % avg_overall_grade

def avg_course_grade(list, course): # функция для определения средней оценки студентов/лекторов по курсу
    avg_grade = []
    for i in list:
        for k, v in i.grades.items():
            if k == course:
                avg_grade.append(v)
                result = sum(sum(avg_grade, [])) / len(sum(avg_grade, []))
    return "%.1f" % result


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students.append(self)


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress\
        and grade in range(1, 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        show = f'Имя: {self.name}\n' \
        f'Фамилия: {self.surname}\n' \
        f'Средняя оценка за домашние задания: {avg_overall_grade(self.grades)}\n' \
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
        f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return show

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Кто-то из них не является студентом!'
        return avg_overall_grade(self.grades) < avg_overall_grade(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturers.append(self)

    def __str__(self):
        show = f'Имя: {self.name}\n' \
        f'Фамилия: {self.surname}\n' \
        f'Средняя оценка за лекции: {avg_overall_grade(self.grades)}'
        return show

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Кто-то из них не является лектором!'
        return avg_overall_grade(self.grades) < avg_overall_grade(other.grades)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        show = f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'
        return show


best_student = Student('John', 'Lennon', 'male')
worst_student = Student('Mick', 'Jagger', 'male')
crazy_student = Student('Axl', 'Rose', 'male')
cool_lecturer = Lecturer('Ivan', 'Ivanov')
boring_lecturer = Lecturer('Boris', 'Borisov')
young_reviewer = Reviewer('Trent', 'Reznor')
old_reviewer = Reviewer('Johnny', 'Cash')

best_student.courses_in_progress += ['Joga', 'Swimming', 'Art']
worst_student.courses_in_progress += ['Joga', 'Swimming', 'Art']
crazy_student.courses_in_progress += ['Joga', 'Swimming', 'Art']
young_reviewer.courses_attached += ['Joga', 'Art']
old_reviewer.courses_attached += ['Joga', 'Art', 'Swimming']
cool_lecturer.courses_attached += ['Joga', 'Swimming', 'Art']
boring_lecturer.courses_attached += ['Joga', 'Swimming', 'Art']

young_reviewer.rate_hw(best_student, 'Joga', 9)
young_reviewer.rate_hw(best_student, 'Art', 10)
young_reviewer.rate_hw(best_student, 'Joga', 8)
young_reviewer.rate_hw(worst_student, 'Joga', 4)
young_reviewer.rate_hw(worst_student, 'Art', 3)
young_reviewer.rate_hw(worst_student, 'Art', 5)
old_reviewer.rate_hw(crazy_student, 'Art', 3)
old_reviewer.rate_hw(crazy_student, 'Art', 6)

best_student.rate_lecturer(cool_lecturer, 'Joga', 10)
best_student.rate_lecturer(cool_lecturer, 'Art', 10)
best_student.rate_lecturer(cool_lecturer, 'Swimming', 9)
best_student.rate_lecturer(boring_lecturer, 'Art', 2)
worst_student.rate_lecturer(boring_lecturer, 'Swimming', 4)
worst_student.rate_lecturer(cool_lecturer, 'Art', 7)
worst_student.rate_lecturer(cool_lecturer, 'Swimming', 7)
#
# print(best_student)
# print()
# print(worst_student)
# print()
# print(cool_lecturer)
# print()
# print(boring_lecturer)
# print()
# print(young_reviewer)
# print()
# print(old_reviewer)
# print()
#
print(best_student.__lt__(worst_student))
print(boring_lecturer.__lt__(cool_lecturer))
#
# print(students)
# print(lecturers)

print(avg_course_grade(students, 'Art'))
print(avg_course_grade(lecturers, 'Swimming'))
