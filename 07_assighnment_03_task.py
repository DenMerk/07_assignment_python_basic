class Student:
    def __init__(self, name, surname, gender, st_average_grade=0):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.st_average_grade = st_average_grade  # Атрибут введен для сравнения средних оценок студентов
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания:\n" \
               f"Курсы в процессе обучения:\n" \
               f"Завершенные курсы:\n"

    def grades_for_lecturer(self, lecturer, course, grade):
        """
        Метод для оценки лекторов студентами
        """
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                course in self.courses_in_progress:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, average_grade=None):
        """
        В данном классе инициализируется только словарь для оценкам лектору от студентов.
        Остальные атрибуты наследуются от родительского класса Mentor
        """
        super().__init__(name, surname)
        self.average_grade = average_grade
        # self.list_of_grades = []
        self.lecturer_grades = {}

    def __str__(self):
        """
        Перегрузка метода для вывода информации о лекторе
        """
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.average_grade}\n"

    def lec_average_grade(self, list_of_grades):
        """
        Метод вычисляет среднюю оценку лектора за прочитанные лекции
        """
        if list_of_grades:
            self.average_grade = sum(list_of_grades) / len(list_of_grades)
        else:
            print(f"У лектора {self.name} {self.surname} нет оценок от студентов")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """
        Метод для выставления оценок студентам
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


def compare_students(students, course):
    """
    Функция для сравнения студентов по их средним оценкам
    """
    best_student_grade = 0
    best_student = None
    for student in students:
        if course in student.courses_in_progress and student.grades[course]:
            student.st_average_grade = sum(student.grades[course]) / len(student.grades[course])
        else:
            print(f"Студент {student.name} {student.surname} не изучает {course} или у него нет оценок")
        if student.st_average_grade > best_student_grade:
            best_student = f"Лучший студент по {course} - {student.name} {student.surname}"
            best_student_grade = student.st_average_grade
    print(best_student)


def compare_lecturers(lecturers, course):
    """
    Функция для сравнения лекторов по оценкам от студентов
    :param lecturers:
    :param course:
    """
    best_lecturer = None
    best_lecturer_grade = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            lecturer.lec_average_grade(lecturer.lecturer_grades[course])
        else:
            print(f"Лектор {lecturer.name} {lecturer.surname} не читает курс по {course}")
        if lecturer.average_grade > best_lecturer_grade:
            best_lecturer = f"Лучший лектор по курсу {course} - {lecturer.name} {lecturer.surname}"
            best_lecturer_grade = lecturer.average_grade
    print(best_lecturer)


student_list = []  # список студентов
lecturer_list = []  # список лекторов

first_student = Student('Петя', 'Петров', 'm')  # инициализация первого студента
student_list.append(first_student)
first_student.courses_in_progress += ['Python']
second_student = Student('Ваня', 'Иванов', 'm')  # второй студент
student_list.append(second_student)
second_student.courses_in_progress += ['Python']

python_reviewer = Reviewer('Python', 'Guru')
python_reviewer.courses_attached += ['Python']
python_reviewer.rate_hw(first_student, 'Python', 10)
python_reviewer.rate_hw(first_student, 'Python', 3)
python_reviewer.rate_hw(first_student, 'Python', 10)

python_reviewer.rate_hw(second_student, 'Python', 9)
python_reviewer.rate_hw(second_student, 'Python', 10)

first_lecturer = Lecturer('Василий', 'Васильев')
first_lecturer.courses_attached += ['Python']
lecturer_list.append(first_lecturer)
second_lecturer = Lecturer('Павел', 'Павлов')
second_lecturer.courses_attached += ['Python']
lecturer_list.append(second_lecturer)
first_student.grades_for_lecturer(first_lecturer, 'Python', 9)
first_student.grades_for_lecturer(second_lecturer, 'Python', 10)
second_student.grades_for_lecturer(first_lecturer, 'Python', 10)
second_student.grades_for_lecturer(second_lecturer, 'Python', 8)

compare_students(student_list, 'Python')
compare_lecturers(lecturer_list, 'Python')

