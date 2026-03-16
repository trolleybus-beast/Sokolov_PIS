#coding:utf-8

groupmates = [
 {
 "name": u"Василий",
 "group": "2251",
 "age": 20,
 "marks": [4, 3, 5, 5, 4]
 },
 {
 "name": u"Анна",
 "group": "2252",
 "age": 22,
 "marks": [3, 2, 3, 4, 3]
 },
 {
 "name": u"Георгий",
 "group": "2253",
 "age": 30,
 "marks": [3, 5, 4, 3, 5]
 },
 {
 "name": u"Валентина",
 "group": "2254",
 "age": 21,
 "marks": [5, 5, 5, 4, 5]}
]

def print_students(students):
    print("Имя студента".ljust(15), "\\",
          "Группа".ljust(8), "\\",
          "Возраст".ljust(8), "\\",
          "Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), "\\",
              student["group"].ljust(8), "\\",
              str(student["age"]).ljust(8), "\\",
              str(student["marks"]).ljust(20))
    print("\n")


def filter_avg_mark(students, avg_mark):
    res = filter(lambda student: (sum(student["marks"]) / len(student["marks"])) > avg_mark, students)
    print_students(res)


filter_avg_mark(groupmates, 4)

