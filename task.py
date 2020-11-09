class Student:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
  
  math_grades = []
  biology_grades = []
  physics_grades = []
  attendence = {}

  def check_attendence(self, day, is_present=0):
    self.attendence[day] = is_present

  def get_total_attendence(self):
    present_sum = 0
    for day in self.attendence:
      present_sum += self.attendence[day]
    return present_sum / len(self.attendence)

  def get_student_average(self):
    all_grades = self.math_grades + self.biology_grades + self.physics_grades
    sum_grades = sum(all_grades)
    average = sum_grades / len(all_grades)
    return average

class Group:
  students = []

  def add_student(self, student):
    self.students.append(student)

  def get_group_average(self):
    sum_averages = 0
    for student in self.students:
      sum_averages += student.get_student_average()
    group_average = sum_averages / len(self.students)
    return group_average

if __name__ == "__main__":

  A = Group()
  B = Group()
  John = Student("John", "Paul")
  Mary = Student("Mary", "Bloody")
  Luke = Student("Luke", "Evangelist")
  Mark = Student("Mark", "Zuckerberg")

  A.add_student(John)
  A.add_student(Mary)
  B.add_student(Luke)
  B.add_student(Mark)
  
  John.math_grades.append(3)
  John.math_grades.append(2)
  John.math_grades.append(4)
  Mary.math_grades.append(3)
  Mary.biology_grades.append(3)
  Luke.math_grades.append(1)
  John.check_attendence("9.11.2020", 1)
  Mary.check_attendence("9.11.2020", 1)
  Luke.check_attendence("9.11.2020", 0)
  Mark.check_attendence("9.11.2020", 1)
  John.check_attendence("10.11.2020", 0)
  Mary.check_attendence("10.11.2020", 0)
  Luke.check_attendence("10.11.2020", 0)
  Mark.check_attendence("10.11.2020", 0)
  
  Mark.get_total_attendence()
  Luke_average = Luke.get_student_average()
  A_average = A.get_group_average()
 