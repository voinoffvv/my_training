grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# список средних значений
sr_grades = list()
for g in grades:
    sr_grades.append(sum(g)/len(g))

# сортируем студентов в алфавитном порядке
students = list(students)
students.sort()

#создает словарь
students_dict = dict()
for i in range(0, len(students)):
    students_dict[students[i]] = sr_grades[i]

print(students_dict)