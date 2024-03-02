# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME Alejandro Olivares-Lopez
# EMAIL OLIVARA5@uci.edu
# STUDENT ID 78845087

import os

def option(directory1, user_input):
    if len(user_input) == 2:
        command_L(directory1)
    elif user_input[2] == "-r":
        contents = command_r(directory1)
        if len(user_input) == 3:
            for items in contents:
                items.strip()
                print(items)
        elif user_input[3] == '-e':
            command_e(contents, user_input)
        elif user_input[3] == '-s':
            command_s(contents, user_input)
        elif user_input[3] == '-f':
            command_f(contents)
    elif user_input[2] == "-f":
        command_f(directory1)
    elif user_input[2] == "-s":
        command_s(directory1, user_input)
    elif user_input[2] == "-e":
        command_e(directory1, user_input)

def option2(command, user_input):
    if command == 'C' and user_input[2] == '-n':
        command_c(user_input[1], user_input)
    elif command == 'D':
        command_d(user_input[1], user_input)
    elif command == 'R':
        command_R(user_input[1], user_input)

def command_R(path, user_input):
    if os.path.exists(path) and os.path.getsize(path) == 0 and path.endswith('.dsu'):
        print("EMPTY")
        main()
    elif os.path.exists(path) and os.path.getsize(path) > 0 and path.endswith('.dsu'):
        with open(f'{path}', 'r') as file1:
            contents = file1.readline()
            print(contents)
            main()
    else:
        print('ERROR')
        main()

def command_d(path, user_input):
    deleted = user_input[1]
    if os.path.exists(path) and path.endswith('.dsu'):
        os.remove(path)
        print(f'{deleted} DELETED')
        main()
    else:
        print("ERROR")
        main()

def command_c(path, user_input):
    extension = 'dsu'
    if os.path.exists(path):
        file_name = user_input[3] + '.' + extension
        dsu_file = os.path.join(path, file_name)
        with open(f'{dsu_file}', 'w') as file1:
            file1.write("")
            print(dsu_file)
    else:
        print("ERROR")
        main()


def command_e(path, user_input):
    if isinstance(path, list):
        for item in path:
            if item.endswith(user_input[len(user_input) - 1]):
                print(item)
    else:
        contents = os.listdir(path)
        for item in contents:
            item_paths = os.path.join(path, item)
            if item_paths.endswith(user_input[len(user_input) - 1]):
                print(item_paths)
    
def command_s(path, user_input):
     if isinstance(path, list):
        for item in path:
            if item.endswith(user_input[len(user_input) - 1]):
                print(item)
     else:
         contents = os.listdir(path)
         for item in contents:
             item_paths = os.path.join(path, item)
             if item_paths.endswith(user_input[len(user_input) - 1]):
                 print(item_paths)


def command_f(path):
    if isinstance(path, list):
        for item in path:
            if '.' in item:
                print(item)
    else:
        contents = os.listdir(path)
        for item in contents:
            item_paths = os.path.join(path, item)
            if os.path.isfile(item_paths):
                print(f'{item_paths}')

def command_r(path):
    result = []
    contents = os.listdir(path)
    for items in contents:
        item_paths = os.path.join(path, items)
        if os.path.isfile(item_paths):
            result.append(item_paths)
        if os.path.isdir(item_paths):
            result.append(item_paths)
            result.extend(command_r(item_paths))
    return result

def command_L(path):
    if os.path.exists(path):
        contents = os.listdir(path)
        for i in range(len(contents)):
            contents[i] = os.path.join(path, contents[i])
        contents = sorted(contents, key = os.path.isdir)
        for items in contents:
            print(items)
    else:
        print(" ")

#Split using whitespace because it is assume that for a valid file to exist or directory there is not space
#but rather using _ or other characters. 
def main():
    user_input = input()
    user_data = user_input.split()
    while user_data[0] != 'Q':
            if user_data[0] == 'L':
                option(user_data[1], user_data)
                user_input = input()
                user_data = user_input.split()
            else:
                if user_data[0] == 'C' and len(user_data) == 1:
                    print("ERROR")
                    main()
                else:
                    option2(user_data[0], user_data)
                    user_input = input()
                    user_data = user_input.split()


if __name__ == "__main__":
    main()
