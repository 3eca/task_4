import os
from sys import argv

''' 1-ый параметр точка старта, 2-ой параметр кол-во выводимых файлов'''

constant_path = argv[1]
number = int(argv[2])


def large_files(size):
    temp_list = []
    size_and_files = {}
    show = os.walk(constant_path)
    for path, directory, files in show:
        path_to_file = str(path) + '\\'
        if files not in temp_list:
            if len(files) > 1:
                for element in files:
                    temp_list.append(path_to_file + element)
            elif len(files) == 1:
                temp_list.append(path_to_file + files[0])
    for element in temp_list:
        size_and_files[os.path.getsize(element)] = element
    temp_list.clear()
    result = sorted(size_and_files.keys(), reverse=True)[:size]
    for index in result:
        yield size_and_files[index]


if __name__ == '__main__':
    # try:
        print(*list(large_files(number)), sep='\n')
    # except Exception:
    #     print('Error read file or error path')
