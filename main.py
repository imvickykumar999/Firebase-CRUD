# https://www.c-sharpcorner.com/article/firebase-crud-operations-using-python/

from imvickykumar999 import firebase
import json

firebase_obj = firebase.FirebaseApplication('https://home-automation-336c0-default-rtdb.firebaseio.com/', None)

def pull():
    result = firebase_obj.get('/esp32/switch/led/', None)

    with open("data.json", "w") as outfile:
        json.dump(result, outfile)

    print('Value fetched = ', result)

def push(data):
    firebase_obj.put('/esp32/switch/','led', data)
    print('updated')

def insert(data):
    result = firebase_obj.post('/esp32/switch/', data)
    print(result)

def remove(result):
    firebase_obj.delete('/esp32/switch/', result)
    print('deleted')

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

if __name__ == "__main__":

    print('''
    Menu...

        1: push(data)
        2: pull()
        3: insert(data)
        4: remove(result)
        0: ...Exit
    ''')

    choice = True
    output = None

    while int(choice):

        try:
            with open('data.json', 'r') as openfile:
              data = json.load(openfile)
        except Exception as e:
            print('''\n   No JSON file present...
            Try Calling Pull method.
            ''')

        choice = input('\n  Enter your Choice : ')

        if choice == '1':
            output = push(data)
        elif choice == '2':
            output = pull()
        elif choice == '3':
            output = insert(data)
        elif choice == '4':
            result = input('\nEnter child name : ')
            output = remove(result)
        else:
            print('Exit...')

        print(output)

    # push(data)
    # pull()

    # result = insert(data)
    # if input("Want to delete ? (1/0) : "):
    #     remove(result)
