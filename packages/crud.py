# Firebase CRUD Tutorial : https://www.c-sharpcorner.com/article/firebase-crud-operations-using-python/

# Create NEW Project : https://console.firebase.google.com/

# My Home Automation Project : https://console.firebase.google.com/u/0/project/home-automation-336c0/database/home-automation-336c0-default-rtdb/data/~2F

from vicksbase import firebase as f
# import json, os
#
# try:
#     os.mkdir('json')
# except Exception as e:
#     print(e)

firebase_obj = f.FirebaseApplication('https://home-automation-336c0-default-rtdb.firebaseio.com/', None)

def push(data, child = 'led'):
    firebase_obj.put('esp32/switch', child, data)
    return ('updated')

def pull(child = 'led'):
    result = firebase_obj.get(f'esp32/switch/{child}', None)

    # with open(f"json/{child}.json", "w") as outfile:
    #     json.dump(result, outfile)
    return ('Value fetched = ', result)

def insert(data = 'hello', child = 'switch/led'):
    result = firebase_obj.post(f'esp32/{child}', data)
    return (result)

def remove(child = 'led'):
    firebase_obj.delete('esp32/switch', child)
    return (pull(child), 'deleted')

# remove('fan')

# def switch(argument):
#     switcher = {
#         1: push(data),
#         2: pull(),
#         3: insert(data),
#         4: remove(result),
#     }
#
#     return switcher.get(argument, "Try Again...")

# output = switch(choice)

#
# if __name__ == "__main__":
#
#     try:
#         with open('data.json', 'r') as openfile:
#           data = json.load(openfile)
#
#     except Exception as e:
#         print('''\n   No JSON file present...
#         Try Calling Pull method.
#         ''')
#
#     print('''
#     Menu...
#
#         1: push
#         2: pull
#         3: insert
#         4: remove
#         0: ...Exit
#     ''')
#
#     choice = True
#     output = None
#
#     while int(choice):
#         choice = input('\n  Enter your Choice : ')
#
#         if choice == '1':
#             output = push(data)
#
#         elif choice == '2':
#             output = pull()
#
#         elif choice == '3':
#             output = insert(data)
#
#         elif choice == '4':
#             child = input('\nEnter child name : ')
#             output = remove(child)
#
#         elif choice == '0':
#             print('Exit...')
#
#         else:
#             print('...try Again !!!')
#
#         print(output)
