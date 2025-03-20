class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"ID: {self.student_id}, 이름: {self.name}, 나이: {self.age}")

class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def display_all_students(self):
        for student in self.students:
            student.display_info()

manager = StudentManager()
student1 = Student(1, "홍길동", 20)
student2 = Student(2, "김철수", 21)
student3 = Student(3, "이영희", 22)

manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)

print("--- 현재 등록된 학생 정보 ---")
manager.display_all_students()


student4 = Student(4, "박민수", 23)
manager.add_student(student4)

print("\n--- 추가 후 전체 학생 정보 ---")
manager.display_all_students()
