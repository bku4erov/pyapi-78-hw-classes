class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress 
                and course in lecturer.courses_attached
                and 0 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def _get_avg_grade(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return sum(all_grades) / len(all_grades)
    
    def __str__(self) -> str:
        return f'Имя: {self.name}\
            \nФамилия: {self.surname}\
            \nСредняя оценка за домашние задания: {self._get_avg_grade()}\
            \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
            \nЗавершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def _get_avg_grade(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return sum(all_grades) / len(all_grades)
    
    def __str__(self) -> str:
        return (super().__str__() + f'\nСредняя оценка за лекции: {self._get_avg_grade()}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
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
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

lecturer_a = Lecturer('John', 'Smith')
lecturer_a.courses_attached += ['Python', 'Git']

best_student.rate_lecture(lecturer_a, 'Python', 10)
best_student.rate_lecture(lecturer_a, 'Python', 10)

print(lecturer_a.grades)
print()

print('Сведения о проверяющем:')
print(cool_reviewer)
print()

print('Сведения о лекторе:')
print(lecturer_a)
print()

print('Сведения о студенте:')
print(best_student)
