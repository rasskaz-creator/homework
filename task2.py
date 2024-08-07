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
    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
   
               

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviews = {}
    
    
        

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
        

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python'] 

 
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

lecturer1 = Lecturer('Honey', 'Bear')
lecturer1.courses_attached += ['Python']
 
reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)

best_student.review(lecturer1, 'Python', 9)
best_student.review(lecturer1, 'Python', 8)
best_student.review(lecturer1, 'Python', 10)

print(best_student.grades)

print(lecturer1.reviews)

