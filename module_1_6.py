my_dict = {'Иванов': 15356.25,
           'Петров': 12547.5,
           'Сидоров': 14228.8}
print(my_dict)
#  Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print(my_dict['Иванов'])
print(my_dict.get('Пантелеев')) # KeyError: 'Пантелеев'

#добавление в словарь
my_dict['Смирнов'] = 19852.7
my_dict['Мамонтов'] = 17544.5
# Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
print(my_dict.pop('Смирнов'))
print(my_dict)

# 3. Работа с множествами:
my_set = {1, 2, 2, 'A', 12.2, (0, 22, 2), 'A'}
print(my_set)
# Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(100)
my_set.add('str')
print(my_set)
# Удалите один любой элемент из множества my_set.
my_set.discard('A')
print(my_set)
