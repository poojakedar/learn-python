"""Day 9: OOP basics (class, object, methods)."""

print("=== Day 9: OOP Basics ===")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")


student1 = Student("Pooja", 21)
student1.add_mark(80)
student1.add_mark(90)
student1.add_mark(70)

student1.show_info()
print("Average:", student1.average())

student2 = Student("Asha", 20)
student2.add_mark(88)
student2.add_mark(92)
student2.show_info()
print("Average:", student2.average())

print("\nDone! Now open exercises/day09_exercises.py")
