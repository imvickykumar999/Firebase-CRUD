# https://www.c-sharpcorner.com/article/firebase-crud-operations-using-python/

from imvickykumar999 import firebase
import json

firebase_obj = firebase.FirebaseApplication('https://home-automation-336c0-default-rtdb.firebaseio.com/', None)

def pull():
    result = firebase_obj.get('/esp32/led/', None)

    with open("data.json", "w") as outfile:
        json.dump(result, outfile)

    print('Value fetched = ', result)


def push(data):
    firebase_obj.put('/esp32','led', data)
    print('updated')

def insert():
    result = firebase_obj.post('/esp32/led/', data)
    print(result)

def remove(result):
    firebase.delete('/esp32/led/', result)
    print('deleted')


if __name__ == "__main__":

    data = { 'Name': 'LED',
              'Value': 1,
              'Switch': 'ON',
              'Cost': 100
            }

    push(data)
    pull() 
