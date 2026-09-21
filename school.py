class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_total_fees(self):
        return sum(student.get_fee() for student in self.students)


class Student:
    def __init__(self, name, fee):
        self.name = name
        self.__fee = fee  # Encapsulation

    # Getter for fee
    def get_fee(self):
        return self.__fee

    # Setter for fee
    def set_fee(self, fee):
        if fee >= 0:
            self.__fee = fee
        else:
            print("Invalid fee amount.")


# Object Creation
school = School("CCS", "Ongole")

student1 = Student("Alice", 7000)
student2 = Student("Bob", 8000)

school.add_student(student1)
school.add_student(student2)

print(f"Total Fees for {school.name}: {school.get_total_fees()}")