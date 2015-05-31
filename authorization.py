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
        elif user_name == credentials[1] and credentials[3] == 'n':
            attempt_counter = 0
            password = input('Enter your password: ')
            while attempt_counter < 3 and password != credentials[2]:
                password = input('Enter your password: ')
                attempt_counter += 1
            if attempt_counter == 3:
                print('Now you are blocked user!(You have used 4 attempts)')
                # TODO create function block_user(credentials[0])
                exit(0)
            return user_name
    file_users.close()



def create_user():
    user_name = input('Create your name: ')
    user_password = input('Create a password: ')
    file_users = open('users.csv', 'r', encoding='utf8')
    last_id = int(file_users.readlines()[-1].split(';')[0])
    file_users.close()
    file_users = open('users.csv', 'a', encoding='utf8')
    file_users.write(str(last_id + 1) + ';' + user_name + ';' + user_password + ';n\n')
    file_users.close()
    return user_name


print(authorization())