#
# with open("new_file.txt") as my_file:
#     read_data = my_file.read()
#
# print(read_data)

# char_read = 15
#
# with open("new_file.txt") as my_file:
#     read_data = my_file.read(char_read)
# actual_length = len(read_data)
# assert actual_length == char_read, "Something went wrong"
# if actual_length == char_read:
#     print("OK")
# else:
#     print("Not OK")
#     exit()
#
# print("Everything is fine")

with open("new_file.txt") as my_file:
    for line in my_file:
        print(line.strip())
