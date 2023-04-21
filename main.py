#Задана рекуррентная функция. Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
# Определить границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
#28.F(1) = 2;
#   F(2) = 4;
#   F(w) = 4*F(w-1)- 3*F(w-2) при w > 2.
from timeit import timeit
import matplotlib.pyplot as plt
a = []
b = []
def paf(w):
    if w == 1:
        return 2
    if w == 2:
        return 4
    if w> 2:
        return 4*paf(w-1) - 3*paf(w-2)
def pav(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n >2:
        fn = [1] * 4
        fn[1] = 2
        fn[2] = 4
        for i in range(3, n+1):
            fn[3] = 4* fn[2] - 3*fn[1]
            fn[0], fn[1],fn[2] = fn[1],fn[2],fn[3]
        return fn[3]
x = [1,2,3,4,5,6,7,8,9,10]
try:
    print(paf(1000))
except:
    print('При вводе 1000 для функции вычисляемой рекурсивно, значение слишком велико и выдаёт ошибку')
print('')
try:
    print("При вводе 1000 для функции, вычисляемой итеративно, получаем следующее значение")
    print(str(pav(1000)))
except:
    print("Ошибка")
print('')
print('№'+'       '+'Рекурсивно'+'        '+'Итеративно')
for i in range(1,11):
    sci1 = 'from __main__ import paf'
    stmti = 'paf('+ str(i)+')'
    sci2 = 'from __main__ import pav'
    stmtj = 'pav('+ str(i)+')'
    a.append(timeit(setup=sci1, stmt= stmti, number=20000))
    b.append(timeit(setup=sci2, stmt= stmtj, number=20000))
    print(str(i) + '|' + str(round(timeit(setup=sci1, stmt= stmti, number=20000),17)) + '|'+ str(round(timeit(setup=sci2, stmt= stmtj, number=20000),17)))
y1 = a
y2 = b
plt.xlabel('Число, которое подаётся')
plt.ylabel('Время поиска')
plt.plot(x, y1, label='Рекурсивно')
plt.plot(x, y2, label='Итеративно')
plt.legend()
plt.show()
