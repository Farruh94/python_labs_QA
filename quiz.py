def check_encoding(file_name):
    rawdata = open(file_name, 'rb').read()
    result = chardet.detect(rawdata)
    charenc = result['encoding']
    print(f"Current file encoding: {charenc}")
    return charenc

import chardet

file_name = "C:\\Users\\LeoKolmanovsky\\Downloads\\python_quiz.txt"

# 1. Read re-format the file
# 2. Create and populate dictionary of questions

with open(file_name, 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    lines = [line for line in lines if not line.startswith('0')]
    lines = [line for line in lines if line.strip()]

"""for line in lines:
    print(line)"""

list_of_questions = []

number_of_lines = len(lines)

for line in lines:
    if line[0].isdigit():
        question = {}
        question['Question'] = ""
        line = line.replace('.', '')
        question['number'] = int(line)
    if line[0] in ("A", "B", "C", "D"):
        question[line[0]] = line[3:]
    else:
        question["Question"] = question["Question"] + "\n" + line

    list_of_questions.append(question)

print(list_of_questions)

"""
{'number': 1,
 'question': "ha-ha-ha",
 'answers': ["A", "B", "C", "D"]
 }
"""
