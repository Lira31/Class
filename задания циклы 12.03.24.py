1.
random_string = 'f1ix_ER8ROR_in_l1ine_&_an7d_B8UG._in_C61o0de!'
correct_string = ""
i = 0
item1 = ""
for item in random_string:
    if item not in ["0","1","2","3","4","5","6","7","8","9","&",".","!"]:
        correct_string = correct_string + item
print(correct_string)
2.
word = input("Введите слово")
a = ["у","ё","е","а","о","э","я","и","ю"]
count = 0
for item in word:
    if item in a:
        count += 1
print(count)
3
random_elements = [3, 6, -9, '-5', 'str', list, 'elem', None, -1, 10, str]
count = 0
b = ""
for a in random_elements:
    if isinstance(a, int):
        count += 1
        if a < 0:
            count -= 1
print(count, -9-5-1)
4.
n = int(input("Введите число"))
for i in range (1, 11):
    print(i * (n-1))
    print(i * n)
    print(i * (n+1))
5.
i = 0
while i < 50:
    a = int(input("Введите число"))
    if i < 50:
        i += a
            
