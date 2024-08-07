class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def review(self, lecturer, course, review):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.reviews:
                lecturer.reviews[course] += [review] 
            else:
                lecturer.reviews[course] = [review] 
        else:
            return 'Ошибка'
    
    def calc_average_grade(self):
        all_grades = []
        
        for grades in self.grades.values():
            all_grades.extend(grades)
            
        if all_grades:
            average_grade = sum(all_grades) / len(all_grades)    
        else:
            average_grade = 0
            
        return  average_grade 
    
    def __str__(self):
        average_grade = self.calc_average_grade()
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {average_grade:.1f}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}"""

    def __lt__(self, other):
        return self.calc_average_grade() < other.calc_average_grade()

    def __le__(self, other):
        return self.calc_average_grade() <= other.calc_average_grade()

    def __gt__(self, other):
        return self.calc_average_grade() > other.calc_average_grade()

    def __ge__(self, other):
        return self.calc_average_grade() >= other.calc_average_grade()

    def __eq__(self, other):
        return self.calc_average_grade() == other.calc_average_grade()

    def __ne__(self, other):
        return self.calc_average_grade() != other.calc_average_grade()
    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}"""
               

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviews = {}
        
    def calc_average_grade(self):
        all_reviews = []
        
        for reviews in self.reviews.values():
            all_reviews.extend(reviews)
            
        if all_reviews:
            average_review = sum(all_reviews) / len(all_reviews)    
        else:
            average_review = 0
            
        return  average_review 
    
    def __str__(self):
        average_review = self.calc_average_grade()
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {average_review:.1f}"""

    def __lt__(self, other):
        return self.calc_average_grade() < other.calc_average_grade()

    def __le__(self, other):
        return self.calc_average_grade() <= other.calc_average_grade()

    def __gt__(self, other):
        return self.calc_average_grade() > other.calc_average_grade()

    def __ge__(self, other):
        return self.calc_average_grade() >= other.calc_average_grade()

    def __eq__(self, other):
        return self.calc_average_grade() == other.calc_average_grade()

    def __ne__(self, other):
        return self.calc_average_grade() != other.calc_average_grade()
        

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
        

def avg_homework_grade(students, course):
    all_grades = []
    count = 0
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
            count += len(student.grades[course])
    if count > 0:
        return sum(all_grades) / count
    else:
        return 0
    
def avg_lecture_review(lecturers, course):
    all_reviews = []
    count = 0
    for lecturer in lecturers:
        if course in lecturer.reviews:
            all_reviews.extend(lecturer.reviews[course])
            count += len(lecturer.reviews[course])
    if count > 0:
        return sum(all_reviews) / count
    else:
        return 0

student1 = Student('Ruoy', 'Eman', 'Male')
student1.courses_in_progress += ['Python'] 
student1.finished_courses += ['Git', 'Math']

student2 = Student('Orange', 'The cat', 'Female')
student2.courses_in_progress += ['Python'] 
student2.finished_courses += ['Git']
 
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Another', 'Buddy')
reviewer2.courses_attached += ['Python']

lecturer1 = Lecturer('Honey', 'Bear')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Flower', 'Bee')
lecturer2.courses_attached += ['Python']
 
reviewer1.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)

student1.review(lecturer1, 'Python', 9)
student1.review(lecturer1, 'Python', 8)
student1.review(lecturer1, 'Python', 10)

reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 6)

student2.review(lecturer2, 'Python', 7)
student2.review(lecturer2, 'Python', 9)
student2.review(lecturer2, 'Python', 6)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)

print(f'Cредняя оценка за домашние задания по всем студентам в рамках Python: {avg_homework_grade([student1, student2], "Python"):.1f}')
print(f'Средняя оценка за лекции всех лекторов в рамках курса Python: {avg_lecture_review([lecturer1, lecturer2], "Python"):.1f}')