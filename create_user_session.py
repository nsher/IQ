# 1) запросить имя
# 2) получить текущее время
# 3) создать файл в директории test_sessions
# 4) записать данные в файл, закрыть

import datetime

user_name = input('Enter your name: ')
d = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
file_name = user_name + "_" + d + ".ts"
f = open('test_sessions/' + file_name, 'w', encoding='utf8')
f.write("info " + file_name)
f.close()