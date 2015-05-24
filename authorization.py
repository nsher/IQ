def authorization():
    user_name = input('Enter your name: ')
    file_users = open('users.csv', 'r', encoding='utf8')
    file_users.readline()
    for line in file_users:
        credentials = line.strip().split(';')
        if user_name == credentials[1] and credentials[3] == 'y':
            print('user is blocked!')
            file_users.close()
            exit(0)
        elif user_name == credentials[1]:
            attempt_counter = 0
            password = input('Enter your password: ')
            while attempt_counter < 4 and password != credentials[2]:
                password = input('Enter your password: ')
                attempt_counter += 1
            if attempt_counter == 4:
                block_user()
    file_users.close()
authorization()
# exit;
# -1 - старой сессии нет
# ID - продолжить старую