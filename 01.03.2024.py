1.
a = str(input("Введите фамилию"))
b = str(input("Введите название страны"))
c = int(input("Введите год"))
d = int(input("Введите стоимость тура"))
e = [a, b , c ,d]
print("Данные о поездке:", e)
2.
a = float(input("Введите а"))
b = float(input("Введите b"))+
c = float(input("Введите c"))
print(a*(b/3.14)+(c*3+5))
3.
r, y = map(float, input("Введите r и y").split())
print(r, y)
4.
a = float(input("Введите a"))
b = a // 1
c = a % 1
print(b, c)
5.
n = int(input("Введите количество минут"))
h = n % (60*24) // 60
m = n % 60
print(h, m)
6.
