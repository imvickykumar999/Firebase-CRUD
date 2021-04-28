# https://www.c-sharpcorner.com/article/firebase-crud-operations-using-python/

# https://console.firebase.google.com/u/0/project/led-blink-wifi/database/led-blink-wifi-default-rtdb/data

from imvickykumar999 import firebase

firebase_obj = firebase.FirebaseApplication('https://led-blink-wifi-default-rtdb.firebaseio.com/', None)

def pull():
    result = firebase_obj.get('/led1/', None)
    print('\n   Value fetched = ', result)

def push(data):
    firebase_obj.put('/','led1', data)
    print('Updated...')


if __name__ == '__main__':

    val = int(input('\n Enter (1/0) : '))
    push(val)

    pull()
