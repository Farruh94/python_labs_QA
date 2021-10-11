# name = input("Привет как тебя зовут?")
# print("Привет", name)

# print("Mars", "Venus", sep="*", end="!")
# print("Mars", "Venus", sep="**", end="?")


# print("Привет ,", input(), end="!")
# this_dict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# this_dict_1 = {
#     "brand": "Chevrolet",
#     "model": "Malibu",
#     "year": 1990
# }
# my_list = [this_dict, this_dict_1]
# for each in my_list:
#     print(each["brand"])
#     print(each["model"])
my_list = ["apple", "cherry", "orange", "kiwi", "melon", "banana", "mango"]
# print(type(my_list))
#
# if type(my_list) == "<class 'list'>":
#     print("That's true")
# else:
#     print("Everything false")
# a = 144
# b = 1444
# print("A") if a > b else print("=") if a == b else print("B")
# if a > b:
#     print("A")
# elif a == b:
#     print("=")
# else:
#     print("B")
# if a > b: print("a is greater than b")

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i in [3, 5]:
#         continue
#     print(i)

# i = 1
# while i < 6:
#     print(i)
#     i += 1
# print("i is no longer less than 6")

# for x in my_list[2]:
#     print(x)
# for i in range(0, 3, 1):
#     print(my_list[i])


def my_function(a, b):
    c = a + b
    return c


first_val = 5
second_val = 7

result = my_function(first_val, second_val)

print(result)