1
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']
m.remove(0.25)
m.remove(15)
m.remove('10')
print(m)
2.
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1:5]
print(abc)
3
numbers = [1, 4]
numbers.insert(1,2)
numbers.insert(2,3)
print(numbers)
4.
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass.sort()
print(mass)
mass.sort(reverse=True)
print(mass)
5.
m1 = []
m2 = []
m3 = []
n = int(input("Введите количество чисел"))
for item in range(1, n+1):
    n1 = int(input("Введите число"))
    if n1 > 0:
        m1.append(n1)
    elif n1 == 0:
        n1 = '*'
