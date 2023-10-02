
# 1
a = int(input("Введи число: "))
print(a)
print(a + 1)
print(a + 2)
# 2
z = 9
x = 11
c = 2
print(int(z+x+c))
# 3
x2 = 25
volume = x2**3
square = 6*x2**2
print("Обьем: ", volume)
print("Площадь: ", square)
# 4
x3 = 1
x4 = 1
res = 3*(x3 + x4)**3 + 275*x3**2 - 127*x4 - 41
print(res)
#5
x5 = int(20)
x6 = x5 - 1
x7 = x5 + 1
print("Следующее за числом", x5, "число: ", x7)
print("Для числа ", x5, "предыдущее число: ", x6)
#6
a1 = 9900
a2 = 55600
a3 = 3999
a4 = 2990
print((a1+a2+a3+a4)*3)
#7
a_1 = -1
d = 1
n = 2
an = a_1 + d * (n - 1)
print(an)
#8
x = 7
result = f"{x}---{2*x}---{3*x}---{4*x}---{5*x}"
print(result)
#9
k = 12
l = 6
rys = l//k
rat = l % k
print(rys, rat)
#10
nn = 2
survivors = (nn + 1) // 2
print(survivors)
#11
number = 50
ress1 = number // 60
resss = number % 60
print(f'{number} мин это -{ress1 }час {resss} минут.')
#12
number = 123
number_str = str(number)
res_sum = int(number_str[0]) + int(number_str[1]) + int(number_str[2])
res_product = int(number_str[0]) * int(number_str[1]) * int(number_str[2])
print("Сумма цифр:", res_sum,)
print("Произведение цифр:", res_product,)
#13
number_of_penguins = input("Укажите число")
print('   _~_    ' * int(number_of_penguins))
print('  (o o)   ' * int(number_of_penguins))
print(' /  V  \\  ' * int(number_of_penguins))
print('/(  _  )\\ ' * int(number_of_penguins))
print('  ^^ ^^   ' * int(number_of_penguins))
#14
abc = 73
k = 1
n = (abc // 10 ** k) % 10
print(n)
#15
n = 150
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)
#16
n0 = 0
print(1 - n0)
#17
nnn = 7
print((nnn//2+1)*2)
#18
v = 60
t = 2
o = v * t
n = o // 109
print(-(109 * n - o))
#19
h = 10
a = 3
b = 2
print((h - a) // (a - b) + 1)