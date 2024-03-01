#1
time = str(input("Какое сейчас время суток?"))
if time == "Утро":
    print("Пора вставать")
elif time == "День":
    print("Пора учиться")
elif time == "Ночь":
    print("Пора спать")
else:
    print("Нет ответа")

#2
password1 = "qwerty123"
password2 = str(input("Ввести пароль"))
if password1 == password2:
    print("Пароль правильный")
else:
    print("Пароль не подходит")

#3
a = input("Отправиться сейчас?")
if a == "да":
    b = input("Все ли припасы погруженны в лодку?")
    if b == "да":
        print("В путь!")
    else:
        print("Стоит подготовиться лучше")
else:
    print("Скажи как будешь готов")

#4
num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
a = input("Что сделать с этими числами?: умножить, разделить, сложить, вычесть")
if a == "умножить":
    print(num1*num2)
elif a == "разделить":
    print(num1//num2)
elif a == "сложить":
    print(num1+num2)
elif a == "вычесть":
    print(num1-num2)
else:
    print("Нет ответа")
#6
n = int(input("Введите число n"))
k = int(input("Введите число k"))
if n%k == 0 or k%n == 0:
    print("Кратно")
else:
    print("Не кратно")

