# abcCBA
# acbCBA
# {{[[(())]]}}
# {{[([())]]}}

def is_balanced(expression):
    my_zip = zip('abc', 'ABC')
    my_map = dict(my_zip)

    print(my_map)
    my_queue = []
    for symbol in expression:
        if symbol in my_map:
            my_queue.append(my_map[symbol])
        else:
            if my_queue:
                last_symbol = my_queue.pop()
                print(last_symbol, " from ", my_queue)
                if symbol != last_symbol:
                    print(my_queue)
                    return False

    return not my_queue


my_expression = input("Введите строку: ").strip()
if is_balanced(my_expression):
    print("String is balanced.")
else:
    print("String is not balanced.")
