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
        if not len(all_grades):
            print(f'The student {self.name} {self.surname} has not got any greades yet!')
            return
        return sum(all_grades) / len(all_grades)
    
    def __str__(self) -> str:
        return f'Имя: {self.name}\
            \nФамилия: {self.surname}\
            \nСредняя оценка за домашние задания: {self._get_avg_grade()}\
            \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
            \nЗавершенные курсы: {", ".join(self.finished_courses)}'
    
    def __lt__ (self, other):
        if not isinstance(other, Student):
            print('Not a Student! Only two students can be compared with each other!')
            return
        if self._get_avg_grade() is None or other._get_avg_grade() is None:
            print('Only students with grades can be compared!')
            return None
        return self._get_avg_grade() < other._get_avg_grade()
    
    def __eq__ (self, other):
        if not isinstance(other, Student):
            print('Not a Student! Only two students can be compared with each other!')
            return
        if self._get_avg_grade() is None or other._get_avg_grade() is None:
            print('Only students with grades can be compared!')
            return None
        return self._get_avg_grade() == other._get_avg_grade()


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
        if not len(all_grades):
            print(f'The lecturer {self.name} {self.surname} has not got any greades yet!')
            return
        return sum(all_grades) / len(all_grades)
    
    def __str__(self) -> str:
        return (super().__str__() + f'\nСредняя оценка за лекции: {self._get_avg_grade()}')
    
    def __lt__ (self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer! Only two lecturer can be compared with each other!')
            return
        if self._get_avg_grade() is None or other._get_avg_grade() is None:
            print('Only lecturers with grades can be compared!')
            return None
        return self._get_avg_grade() < other._get_avg_grade()
    
    def __eq__ (self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer! Only two lecturer can be compared with each other!')
            return
        if self._get_avg_grade() is None or other._get_avg_grade() is None:
            print('Only lecturers with grades can be compared!')
            return None
        return self._get_avg_grade() == other._get_avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Create 2 instances of each class

# Create 2 instances of class Student
student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Jenny', 'Smith', 'female')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['JavaScript']
student_2.finished_courses += ['Введение в программирование']

# Create 2 instances of class Reviewer
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Helen', 'Green')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['JavaScript']

# Create 2 instances of class Lecturer
lecturer_1 = Lecturer('John', 'Smith')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Ivan', 'Ivanov')
lecturer_2.courses_attached += ['Python', 'JavaScript']

# Create 2 instances of class Mentor
mentor_1 = Mentor('Petr', 'Petrov')
mentor_1.courses_attached += ['Python']

mentor_2 = Mentor('John', 'Brown')
mentor_2.courses_attached += ['Git']


# Call all created methods of the classes

# Call Student's method to rate lectures
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Git', 10)
student_1.rate_lecture(lecturer_2, 'Python', 10)
student_2.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'JavaScript', 10)

# Call Reviewer's method to rate student's homework
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'JavaScript', 10)

# Call overloaded __str__method of all clases
# also protected method to calculate mean grade will be called from __str__ method
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(mentor_1)
print(mentor_2)

# Call overloaded methods to compare instances of classes by their mean grade
print(student_1 < student_2)
print(student_1 > student_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 == lecturer_2)