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

    def _stu_average_grade(self, list_of_grades):
        """
        Метод для расчета средней оценки студета по предмету
        """
        self.st_average_grade = 0
        if list_of_grades:
            self.st_average_grade = sum(list_of_grades) / len(list_of_grades)
        return self.st_average_grade

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

    def __lt__(self, other):
        """
        Перегрузка метода сравнения для определения лучшего студента
        """
        if isinstance(other, Student):
            best_student = other.surname
            if other._stu_average_grade(other.grades['Python']) < self._stu_average_grade(self.grades['Python']):
                best_student = self.surname
            return f"Студент {best_student} имеет лучшие оценки"
        else:
            print(f"Недопустимые данные")

    def __gt__(self, other):
        """
        Перегрузка метода сравнения для определения лучшего студента (для второго оператора сравнения)
        """
        if isinstance(other, Student):
            best_student = other.surname
            if self._stu_average_grade(self.grades['Python']) > other._stu_average_grade(other.grades['Python']):
                best_student = self.surname
            return f"Студент {best_student} имеет лучшие оценки"
        else:
            print(f"Недопустимые данные")


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

    def _lec_average_grade(self, list_of_grades):
        """
        Метод вычисляет среднюю оценку лектора за прочитанные лекции
        """
        if list_of_grades:
            self.average_grade = sum(list_of_grades) / len(list_of_grades)
            return self.average_grade
        else:
            print(f"У лектора {self.name} {self.surname} нет оценок от студентов")

    def __lt__(self, other):
        """
        Перегрузка метода сравнения для определению лектора с наилучшими оценками
        """
        if isinstance(other, Lecturer):
            best_lecturer = self.surname
            if self._lec_average_grade(self.lecturer_grades['Python']) < \
                    other._lec_average_grade(other.lecturer_grades['Python']):
                best_lecturer = other.surname
            return f"Лектор {best_lecturer} имеет самые высокие оценки от студентов"
        else:
            print('Недопустимые данные')

    def __gt__(self, other):
        """
        Перегрузка метода сравнения для определению лектора с наилучшими оценками (для второго оператора сравнения)
        """
        if isinstance(other, Lecturer):
            best_lecturer = other.surname
            if self._lec_average_grade(self.lecturer_grades['Python']) > \
                    other._lec_average_grade(other.lecturer_grades['Python']):
                best_lecturer = self.surname
            return f"Лектор {best_lecturer} имеет самые высокие оценки от студентов"
        else:
            print('Недопустимые данные')


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
# python_reviewer.rate_hw(first_student, 'Python', 3)
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
second_student.grades_for_lecturer(second_lecturer, 'Python', 10)

print(first_student < second_student)
print(first_lecturer > second_lecturer)
