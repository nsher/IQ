import os


def get_last_unclosed_results(user_name):
    path = './test_sessions/'
    last_file_name = ''
    for name in os.listdir(path):
        #print(name[:len(user_name)])
        #if os.path.isfile(os.path.join(path, name)) and name.split('_')[0] == user_name:
        if name.split('_')[0] == user_name and name[-3:] == '.ts':
            f = open(path + name, 'r', encoding='utf8')
            if 'Test is finished.' not in f.read():
                last_file_name = name
            f.close()
    return last_file_name

# file_names = get_last_unclosed_results('m') # empty
file_names = get_last_unclosed_results('neil') # neil_2015-05-03-21-34.ts
# file_names = get_last_unclosed_results('n') # empty
print(file_names)