# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных 
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

S = int(input('Сумма чисел: '))
P = int(input('Произведение чисел: '))
for i in range(S):
    for j in range(P):
        if S == i + j and P == i * j:
            print(i, j)
            



# import math
# S = int(input('Сумма чисел: '))
# P = int(input('Произведение чисел: '))
# D = int(math.sqrt(S**2-(4*1*P)))
# x1 = int((- S + D)/-2)
# x2 = int((- S - D)/-2)
# y1 = S-x1
# y2 = S-x2
# print(f"Число X = {x1}, число Y = {y1}")