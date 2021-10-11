# Data Types
# Приведенный пример кода выведет на консоль тип данных переменной x, какой это будет тип?

x = 5
print(type(x))
x = "Hello World!"
print(type(x))
x = 20.5
print(type(x))
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = {"name": "John", "age": 36}
print(type(x))
x = True
print(type(x))

# Numbers
# У вас есть приведенный ниже код. Восстановите пропущенную строку (...), чтобы в результате выполнения кода на консоли
# появилось указанное сообщение

x = 5
x = (float(x))
print(x, type(x))

x = 5
x = (int(x))
print(x, type(x))

# Strings
# Воспользуйтесь методом len(), чтобы определить длину строки

x = "Hello World"
print(len(x))

txt = "Hello World!"
x = txt[0]
print(x)

x = "Hello World!"
print(x[1:5])

a = "Hello World"
b = " Hello World "
if a == b:
    print(True)
else:
    print(b.strip())

y = "Hello World"
print(y.upper())
print(y.lower())
print(y.replace("H", "J"))
print(y.replace("World", "Word"))

my_age = 27
txt = "I am {} years old"
print(txt.format(my_age))

import random
txt = "I made this mistake {} times"
print(txt.format(random.randrange(1, 150)))

import string
length = 25
print("Random user name with:")
print("".join(random.choices(string.ascii_letters, k=length)))