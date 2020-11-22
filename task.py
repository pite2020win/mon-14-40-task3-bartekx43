import json
from statistics import mean
from statistics import StatisticsError

def add_school(system, school_name):
  system[school_name] = {}

def add_class(system, school, group_name):
  system[school][group_name] = {}

def add_student(system, school, group, ID, name, surname):
  system[school][group][ID] = {"name": (name, surname), "grades": [], "attendance": []}

def add_grade(system, school, group, ID, grade):
  system[school][group][ID]["grades"].append(grade)

def check_attendance(system, school, group, ID, if_present):
  system[school][group][ID]["attendance"].append(if_present)

def get_student_info_by_name(system, name, surname):
  for school in system:
    for group in system[school]:
      for ID in system[school][group]:
        if system[school][group][ID]["name"] == (name, surname):
          stud = system[school][group][ID]
          info = f"Name: {stud['name'][0]}\n"\
                  f"Surname: {stud['name'][1]}\n"\
                  f"School: {school}\n"\
                  f"Class: {group}\n"\
                  f"Grades: {stud['grades']}"
          return info  

def get_student_average(system, school, group, ID):
  try:
    average =  mean(system[school][group][ID]["grades"])
    round_average = round(average, 2)
  except StatisticsError:
    round_average = 0
  return round_average

def get_student_attendance_percent(system, school, group, ID):
  attendance = system[school][group][ID]["attendance"]
  ratio = sum(attendance)/len(attendance)
  return round(ratio, 2)

def get_group_grades(system, school, group):
  group_grades = []
  for ID in system[school][group]:
    group_grades.extend(system[school][group][ID]["grades"])
  return group_grades

def get_group_average(system, school, group):
  group_grades = get_group_grades(system, school, group)
  try:
    group_average = mean(group_grades)
    round_group_average = round(group_average, 2)
  except StatisticsError:
    group_average = 0
  return round_group_average

def get_school_grades(system, school):
  school_grades = []
  for group in system[school]:
    school_grades.extend(get_group_grades(system, school, group))
  return school_grades

def get_students_in_class(system, school, group):
  group_students = list(map(lambda x: system[school][group][x]["name"], system[school][group]))
  return group_students

def get_students_in_school(system, school):
  all_students = list(map(lambda x: get_students_in_class(system, school, x), system[school]))
  return all_students

def read_system_from_json(file_name):
  with open(file_name) as f:
    system = json.load(f)
    return system

def save_to_json(system, file_name):
  with open(file_name, 'w') as f:
   json.dump(system, f, indent=1)

if __name__ == "__main__":
  file_name = "data.json"
  system = read_system_from_json(file_name)

  add_school(system, "school1")
  add_school(system, "school2")

  add_class(system, "school1", "A")
  add_class(system, "school1", "B")
  add_class(system, "school2", "A")

  add_student(system, "school1", "A", 0, "John", "Kerry")
  add_student(system, "school1", "A", 1, "Barack", "Obama")
  add_student(system, "school1", "B", 2, "Joe", "Biden")
  add_student(system, "school1", "B", 3, "Kamala", "Harris")
  add_student(system, "school1", "B", 4, "Elisabeth", "Warren")
  add_student(system, "school1", "B", 5, "Martin", "Luther")
  add_student(system, "school2", "A", 6, "Ronald", "Reagan")
  add_student(system, "school2", "A", 7, "Hillary", "Clinton")
  add_student(system, "school2", "A", 8, "George", "Soros")
  add_student(system, "school2", "A", 9, "Victor", "Orban")
  add_student(system, "school2", "A", 10, "Bill", "Gates")
  add_student(system, "school2", "A", 11, "Vlad", "Putin")

  add_grade(system, "school1", "A", 0 , 3)
  add_grade(system, "school1", "A", 0, 4)
  add_grade(system, "school1", "A", 1, 4)
  add_grade(system, "school1", "B", 5, 3)
  add_grade(system, "school1", "B", 5, 4)
  add_grade(system, "school1", "B", 5, 1)
  add_grade(system, "school2", "A", 8, 5)
  add_grade(system, "school2", "A", 8, 3)

  check_attendance(system, "school2", "A", 8, 1)
  check_attendance(system, "school2", "A", 8, 0)
  check_attendance(system, "school2", "A", 8, 1)
  check_attendance(system, "school1", "B", 4, 1)
  check_attendance(system, "school1", "B", 5, 1)
  check_attendance(system, "school1", "A", 1, 0)

  save_to_json(system, file_name)

######################################################

  print(get_student_average(system, "school1", "B", 5))
  print(get_group_average(system, "school1", "A"))
  print(get_student_attendance_percent(system, "school2", "A", 8))
  print(get_student_info_by_name(system, "Barack", "Obama"))
  print(get_school_grades(system, "school1"))
  print(get_students_in_class(system, "school1", "A"))
  print(get_students_in_school(system, "school2"))


