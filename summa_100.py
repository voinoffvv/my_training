# Задача
# У вас есть девять цифр: 1, 2, 3, 4, 5, 6, 7, 8, 9, расположенных в указанном порядке. 
# Вам необходимо вставить между ними знаки «+», «-» или оставить пробел, чтобы получить выражения, подобные 123+45-6+7+89. 
# Задача состоит в том, чтобы найти все такие выражения, которые в итоге равны 100.

def all_combinations(a): # все комбинации цифр
    if len(a) <= 1:
        yield a
    else:
        head = ''
        tail = list(a)
        while len(tail) > 0:
            head += tail.pop(0)
            for s in all_combinations(tail):
                yield [head] + s
# print(list(all_combinations('123456789')))

def all_signs(n): # все комбинации знаков для количества цифр
    if n ==0:
        yield()
    else:
        for tail in all_signs(n - 1):
            for s in '+-':
                yield (s, ) + tail
#print(list(all_signs(10)))

def perfom_operations(nums, signs):
    nums = list(map(int, nums))
    res = nums.pop(0)
    for s in signs:
        if s == '+':
            res += nums.pop(0)
        if s == '-':
            res -= nums.pop(0)
    return res

stroka1 = '123456789'
for numbers in all_combinations(stroka1):
    for ss in all_signs(len(numbers) - 1):
        summ = perfom_operations(numbers, ss)
        if summ == 100:
            # print(list(zip(numbers, ss)))
            print(' '.join(map(lambda x: ' '.join(x), zip(numbers, ss))) + ' ' + numbers[-1] + ' = ' + str(summ))
        
# 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100
# 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100
# 1 + 23 - 4 + 5 + 6 + 78 - 9 = 100
# 1 + 23 - 4 + 56 + 7 + 8 + 9 = 100
# 12 - 3 - 4 + 5 - 6 + 7 + 89 = 100
# 12 + 3 + 4 + 5 - 6 - 7 + 89 = 100
# 12 + 3 - 4 + 5 + 67 + 8 + 9 = 100
# 123 - 4 - 5 - 6 - 7 + 8 - 9 = 100
# 123 + 4 - 5 + 67 - 89 = 100
# 123 + 45 - 67 + 8 - 9 = 100
# 123 - 45 - 67 + 89 = 100