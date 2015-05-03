#!/usr/bin/python
import random, sys, math, re, datetime


def iq(level, user_name): # весь тест
    max_result = 0
    result = 0
    d = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
    file_name = 'test_sessions/' + user_name + "_" + d + ".ts"
    file_results = open(file_name, 'w', encoding='utf8')
    file_questions = open(level + ".iq", "r", encoding="utf8")
    print('test run in ' + level + ' mode')
    file_results.write(level + '\n')
    file_results.close()
    for line in file_questions:
        current_result = question(line, file_name)
        result += current_result
        max_result += 5
    file_questions.close()
    percent = math.ceil(result / max_result * 100)
    message = '| Test is finished. Your result is ' + str(result)
    message += ' out of ' + str(max_result) + ' (' + str(percent) + '%) |'
    to_results = ' ' + '-' * (len(message) - 2) + '\n'
    to_results += message + '\n'
    to_results += ' ' + '-' * (len(message) - 2) + '\n'
    to_results += get_message(percent) + '\n'
    print(to_results)
    file_results = open(file_name, 'a', encoding='utf8')
    file_results.write(to_results)
    file_results.close()


def question(src, fname): # вывод и обработка ответа по вопросу, src - строка из файла с вопросами
    a = src.strip().split(';')
    if len(a) == 3:
        question, answers, correct_answers = a[0], a[1], a[2]
        correct_answers = correct_answers.split()
    else:
        question, answers, correct_answers = a[0], '', [0]
        correct_answers = [0]
        if '${a}' in src:
            a = random.randint(1, 1000)
            question = question.replace('${a}', str(a))
        if '${b}' in src:
            b = random.randint(1, 1000)
            question = question.replace('${b}', str(b))
        if '${+}' in src:
            correct_answers[0] = str(a + b)
            question = question.replace('${+}', '+')
        if '${*}' in src:
            correct_answers[0] = str(a * b)
            question = question.replace('${*}', '*')
        if '${?}' in src:
            correct_answers[0], operator = computeExpression(a, b)
            question = question.replace('${?}', operator)
            if operator == '/':
                print('hint: answer ceil to nearest integer')
    m = re.match(r".*?(\$\{(pic\d+\.txt)\}).*?", question) # анализ исходной строки - поиск вхождения имени файла в
    if m is not None:
        question = question.replace(m.group(1), '')
        f = open('pictures/' + m.group(2))
        for line in f:
            print(line, end='')
        print()
        f.close()
    print(question)
    if answers != '':
        print(answers)
    user_answer = input()
    current_result = 0
    if str(correct_answers[0]) == user_answer.strip():
        current_result += 5
    elif len(correct_answers) > 1 and correct_answers[1] == user_answer:
        current_result += 2
    elif len(correct_answers) > 2 and correct_answers[2] == user_answer:
        current_result += 1
    file = open(fname, 'a', encoding='utf8')
    file.write('you got ' + str(current_result) + ' score for question: ' + question + '\n')
    file.close()
    return current_result


def get_message(iq_percentage): # получение псевдографического ASCII сообщения
    file = open('messages.txt')
    strings = file.readlines()
    file.close()
    if iq_percentage in range(75, 101):  # genius
        rng = range(0, 9)
    elif iq_percentage in range(50, 75):  # clever
        rng = range(9, 18)
    elif iq_percentage in range(25, 50):  # good
        rng = range(18, 27)
    elif iq_percentage in range(0, 25):  # done
        rng = range(27, 36)
    else:
        rng = range(0, 0)
    message = ''
    for i in rng:
        message += strings[i][:]
    return message


def computeExpression(x, y): # генерация арифметического примера из двух случайных чисел, результат - ответ и оператор
    randOp = random.randint(0, 5)
    operators = ['+', '-', '*', '/', '//', '%']
    if randOp == 0:
        return x + y, operators[randOp]
    if randOp == 1:
        return x - y, operators[randOp]
    if randOp == 2:
        return x * y, operators[randOp]
    if randOp == 3:
        return math.ceil(x / y), operators[randOp]
    if randOp == 4:
        return x // y, operators[randOp]
    if randOp == 5:
        return x % y, operators[randOp]


def main(): # основная функция программы
    user_name = input('Enter your name: ')
    modes = ['easy', 'difficult', 'hard', 'extreme']
    if len(sys.argv) == 2: # если программа запущена из командной строки и ей передан аргумент - имя уровня
        mode = sys.argv[1]
    else: # запрос уровня у пользователя (до тех пор, пока не укажет корректно)
        print('easy or difficult, hard, extreme')
        mode = input()
        while mode not in modes:
            print('type correct mode name!')
            mode = input()
    iq(mode, user_name)


if __name__ == "__main__":
    main()