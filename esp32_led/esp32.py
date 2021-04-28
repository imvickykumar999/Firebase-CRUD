# https://www.c-sharpcorner.com/article/firebase-crud-operations-using-python/

# https://console.firebase.google.com/u/0/project/led-blink-wifi/database/led-blink-wifi-default-rtdb/data

# ==============================================

from vicksbase import firebase

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
    input('\n   Click Enter to Exit...')

# =================================================

# from firebase import firebase
# fb_app = firebase.FirebaseApplication('https://led-blink-wifi-default-rtdb.firebaseio.com/', None)
# result = fb_app.get('/led1', None)
# input(result)

# C:\Users\Vicky\Desktop\Repository\firebase\Firebase-CRUD>python esp32.py
# Traceback (most recent call last):
#   File "esp32.py", line 25, in <module>
#     from firebase import firebase
# ImportError: cannot import name 'firebase' from 'firebase' (unknown location)
