class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
    def __init__(self, name, surname):
        """
        В данном классе инициализируется только словарь для оценкам лектору от студентов.
        Остальные атрибуты наследуются от родительского класса Mentor
        """
        super().__init__(name, surname)
        self.lecturer_grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """
        Перенос метода для выставления оценок студентам из
        родительского класса Mentor в дочерний Reviewer
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

python_reviewer = Reviewer('Python', 'Guru')
python_reviewer.courses_attached += ['Python']
python_reviewer.rate_hw(best_student, 'Python', 10)


git_lecturer = Lecturer('Git', 'Jedi')
git_lecturer.courses_attached += ['Git']
best_student.grades_for_lecturer(git_lecturer, 'Git', 10)
best_student.grades_for_lecturer(git_lecturer, 'Git', 9)


print(f'Оценки лектора {git_lecturer.name} {git_lecturer.surname} {git_lecturer.lecturer_grades["Git"]}')

print(f'Оценки студента {best_student.name} {best_student.surname} {best_student.grades["Python"]}')
