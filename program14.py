import pickle
import shelve

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


student = Student("Rahul", 101, 92)

# Serialization using pickle
with open("student.dat", "wb") as file:
    pickle.dump(student, file)

print("Object saved using pickle.")

# Deserialization using pickle
with open("student.dat", "rb") as file:
    restored_student = pickle.load(file)

print("\nRestored object using pickle:")
restored_student.display()

# Persistence using shelve
with shelve.open("student_db") as db:
    db["student"] = student

print("\nObject saved using shelve.")

# Restore object using shelve
with shelve.open("student_db") as db:
    restored = db["student"]

print("\nRestored object using shelve:")
restored.display()
