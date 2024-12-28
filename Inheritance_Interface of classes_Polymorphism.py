#Inheritance, attributes of classes and interface, polymorphism

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        sum_grades = 0
        n_gr = 0
        for grade in self.grades.values():
            sum_grades += sum(list(grade))
            n_gr += len(grade)
        self.average_rating = round((sum_grades / n_gr), 1)
        output = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_rating}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return output

    def __lt__(self, other):
        """Сравнение студентов между собой по средней оценке за домашние задания через оператор '<'"""
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.average_rating < other.average_rating

    def __gt__(self, other):
        """Сравнение студентов между собой по средней оценке за домашние задания через оператор '<'"""
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.average_rating > other.average_rating

    def __eq__(self, other):
        """Сравнение студентов между собой по средней оценке за домашние задания через оператор '<'"""
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.average_rating == other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.lecturers_list = []
        self.average_rating = float()

    def __eq__(self, lect):
        if not isinstance(lect, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_rating == lect.average_rating

    def __lt__(self, lect):
        if not isinstance(lect, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_rating < lect.average_rating

    def __gt__(self, lect):
        if not isinstance(lect, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_rating > lect.average_rating

    def __str__(self):
        grades_count = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
        self.average_rating = round(sum(map(sum, self.grades.values())) / grades_count, 1)
        output = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.average_rating}\n'
        return output


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}  \n"


#Define people and courses according to roles
#Student1
some_student1 = Student('Ruoy', 'Eman', 'man')
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.finished_courses += ['Java', 'C++']

#Student2
some_student2 = Student('Alexey', 'Petrov', 'man')
some_student2.courses_in_progress += ['Python']
some_student2.finished_courses += ['Java']

#Reviewer1
some_reviewer1= Reviewer('Some', 'Buddy')
some_reviewer1.courses_attached += ['Python', 'Java', 'C++', 'Csharp', 'Git']

#Reviewer2
some_reviewer2= Reviewer('Another', 'Buddy')
some_reviewer2.courses_attached += ['Python', 'Java', 'C++', 'Csharp', 'Git']

#Lecturer1
some_lecturer1 = Lecturer("Some", "Buddy")
some_lecturer1.courses_attached += ['Python', 'Java', 'C++', 'Csharp', 'Git']

#Lecturer2
some_lecturer2 = Lecturer("Ivan", "Ivanov")
some_lecturer2.courses_attached += ['Python', 'Java', 'Git']


#Actions with student1
some_student1.rate_lecturer(some_lecturer1, 'Python', 8)
some_student1.rate_lecturer(some_lecturer2, 'Python', 9)
some_student1.rate_lecturer(some_lecturer1, 'Git', 6)

#Actions with student2
some_student2.rate_lecturer(some_lecturer1, 'Python', 3)
some_student2.rate_lecturer(some_lecturer2, 'Python', 6)
some_student2.rate_lecturer(some_lecturer2, 'Git', 3)
some_student2.rate_lecturer(some_lecturer2, 'Git', 10)

#Actions with reviewer1
some_reviewer1.rate_hw(some_student1, 'Python', 5)
some_reviewer1.rate_hw(some_student1, 'Git', 10)
some_reviewer1.rate_hw(some_student2, 'Python', 1)
some_reviewer1.rate_hw(some_student2, 'Python', 5)

#Actions with reviewer2
some_reviewer2.rate_hw(some_student1, 'Git', 2)
some_reviewer2.rate_hw(some_student1, 'Git', 5)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 3)


#print grades of students
print(f"Grades of student \t |{some_student1.name} {some_student1.surname}|\t\t for courses:\t\t\t{some_student1.grades}")
print(f"Grades of student \t |{some_student2.name} {some_student2.surname}|\t for courses:\t\t\t{some_student1.grades}")

#print grades of lecturers
print(f"Grades of lecturer \t |{some_lecturer1.name} {some_lecturer1.surname}|\t\t for conducted_courses:\t{some_lecturer1.grades}")
print(f"Grades of lecturer \t |{some_lecturer2.name} {some_lecturer2.surname}|\t\t for conducted_courses:\t{some_lecturer2.grades}")

#print data
for elem in (some_student1, some_student2):
    print(f"\nStudent\n{elem}")

for elem in (some_lecturer1, some_lecturer2):
    print(f"\nLecturer\n{elem}")

for elem in (some_reviewer1, some_reviewer2):
    print(f"\nReviewer\n{elem}")

#Comparison of average lecturers' grades
lect_comparison1 = f"Средняя оценка лектора '{some_lecturer1.name} {some_lecturer1.surname}' по проводимым курсам {some_lecturer1.courses_attached}\n" \
                   f"одинакова средней оценке лектора '{some_lecturer2.name} {some_lecturer2.surname}'? \n{some_lecturer1.__eq__(some_lecturer2)}\n"
lect_comparison2 = f"Средняя оценка лектора '{some_lecturer1.name} {some_lecturer1.surname}' по проводимым курсам {some_lecturer1.courses_attached}\n" \
                   f"выше средней оценки лектора '{some_lecturer2.name} {some_lecturer2.surname}'? \n{some_lecturer1.__gt__(some_lecturer2)}\n"
lect_comparison3 = f"Средняя оценка лектора '{some_lecturer1.name} {some_lecturer1.surname}' по проводимым курсам {some_lecturer1.courses_attached}\n" \
                   f"ниже средней оценки лектора '{some_lecturer2.name} {some_lecturer2.surname}'? \n{some_lecturer1.__lt__(some_lecturer2)}\n"

print(lect_comparison1)
print(lect_comparison2)
print(lect_comparison3)

#Comparison of average students' grades
stud_comparison1 = f"Средняя оценка студента '{some_student1.name} {some_student1.surname}' выше средней оценки студента '{some_student2.name} {some_student2.surname}'?\n{some_student1.__gt__(some_student2)}"
stud_comparison2 = f"Средняя оценка студента '{some_student1.name} {some_student1.surname}' эквивалентна средней оценке студента '{some_student2.name} {some_student2.surname}'?\n{some_student1.__eq__(some_student2)}"
stud_comparison3 = f"Средняя оценка студента '{some_student1.name} {some_student1.surname}' выше средней оценки студента '{some_student2.name} {some_student2.surname}'?\n{some_student1.__lt__(some_student2)}"

print(stud_comparison1)
print(stud_comparison2)
print(stud_comparison3)

# Создаем список студентов
student_list = [some_student1, some_student2]

# Создаем список лекторов
lecturer_list = [some_lecturer1, some_lecturer2]

def average_student_rating(student_list, course_title):
    """Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    в качестве аргументов принимает список студентов и название курса"""

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_title]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all_courses = round(sum_all / count_all, 1)
    return average_for_all_courses


def average_lecturer_rating(lecturer_list, course_title):
    """Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
     в качестве аргумента принимает список лекторов и название курса"""

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_title]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all_courses = round(sum_all / count_all, 1)
    return average_for_all_courses


# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"\nСредняя оценка для всех студентов по курсу {'Python'}: {average_student_rating(student_list, 'Python')}")
print()
