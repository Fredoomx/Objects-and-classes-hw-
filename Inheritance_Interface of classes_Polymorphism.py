#Inheritance, attributes of classes and interface, polymorphism

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_student_grade(self):
        sum_grades = 0
        n_gr = 0
        for grade in self.grades.values():
            sum_grades += sum(list(grade))
            n_gr += len(grade)

        av_grade = round((sum_grades / n_gr), 1)
        return av_grade

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_student_grade()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)} \n"


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

    def average_lecturer_grade(self):
        sum_grades = 0
        n_gr = 0
        for grade in self.grades.values():
            sum_grades += sum(list(grade))
            n_gr += len(grade)

        av_grade = round((sum_grades / n_gr), 1)
        return av_grade

    def av_lect_grade_by_course(self, lecturers_list, course_title):
        sum_grades = 0
        n_gr = 0
        for lector in lecturers_list:
            if lector.grades == course_title:
                for grade in lector.grades.values():
                    sum_grades += sum(list(grade))
                    n_gr += len(grade)
            else:
                pass

        av_lect_grade_by_course = round((sum_grades / n_gr), 1)
        return av_lect_grade_by_course

    def __eq__(self, lecturer):
        return self.average_lecturer_grade() == lecturer.average_lecturer_grade()

    def __lt__(self, lecturer):
        return self.average_lecturer_grade() < lecturer.average_lecturer_grade()

    def __gt__(self, lecturer):
        return self.average_lecturer_grade() > lecturer.average_lecturer_grade()

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_lecturer_grade()} \n"


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

# class Course:
#     def __init__(self):
#
#         self.course_title = course_title
#
#
# python_course = Course('Python')
# git_course = Course('Git')


#Define people and courses according to roles
#Student1
some_student1 = Student('Ruoy', 'Eman', 'man')
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.finished_courses += ['Java', 'C++']

#Student2
some_student2 = Student('Alexey', 'Petrov', 'man')
some_student2.courses_in_progress += ['Python']
some_student2.finished_courses += ['Java']

#list of students
student_list = [some_student1, some_student2]

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

#List of lecturers
lecturers = [some_lecturer1, some_lecturer2]
average_course_grade = Lecturer.av_lect_grade_by_course(lecturers, )

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

#print average grades by courses



#print data
for elem in (some_student1, some_student2):
    print(f"\nStudent\n{elem}")

for elem in (some_lecturer1, some_lecturer2):
    print(f"\nLecturer\n{elem}")

for elem in (some_reviewer1, some_reviewer2):
    print(f"\nReviewer\n{elem}")

#Comparison of average lecturers' grades
print(f"Средняя оценка лектора '{some_lecturer1.name} {some_lecturer1.surname}' по проводимым курсам {some_lecturer1.courses_attached} одинакова остальным? \n{some_lecturer1.__eq__(some_lecturer2)}\n")
print(f"Средняя оценка лектора '{some_lecturer1.name} {some_lecturer1.surname}' по проводимым курсам {some_lecturer1.courses_attached} выше? \n{some_lecturer1.__gt__(some_lecturer2)}\n")
print(f"Средняя оценка лектора '{some_lecturer1.name} {some_lecturer1.surname}' по проводимым курсам {some_lecturer1.courses_attached} ниже? \n{some_lecturer1.__lt__(some_lecturer2)}\n")