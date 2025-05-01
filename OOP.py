class Student:
    def __init__(self, name, age, form):
        self.name = name
        self.age = age
        self.form = form
        self.subjects = [] 
        self.marks = {}


    def add_subject(self, subject):
        self.subjects.append(subject)
        self.marks[subject] = None  # Initialize marks for the new subject as None

 
    def add_marks(self, subject, mark):
        if subject in self.marks:
            self.marks[subject] = mark
        else:
            print(f"Subject '{subject}' not found!")

    def average_marks(self):
        total_marks = sum(mark for mark in self.marks.values() if mark is not None)
        num_subjects = sum(1 for mark in self.marks.values() if mark is not None)
        
        if num_subjects == 0:
            return 0  # Avoid division by zero if no marks are entered
        return total_marks / num_subjects

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Form: {self.form}")
        print(f"Subjects: {', '.join(self.subjects)}")
        print("Marks:")
        for subject, mark in self.marks.items():
            mark_display = mark if mark is not None else "Not entered yet"
            print(f"  {subject}: {mark_display}")
        print(f"Average Marks: {self.average_marks():.2f}")

student1 = Student("Samuel", 23, "Form Four")
student1.add_subject("Math")
student1.add_subject("English")
student1.add_marks("Math", 90)
student1.add_marks("English", 85)

student1.display_info()
