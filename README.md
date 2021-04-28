# Firebase-CRUD
  Home Automation using my firebase package and kivy Android App, finally display output on my website.

## Create new file in cmd
  type nul > led.py

## Code...

  from imvickykumar999 import firebase

  firebase_obj = firebase.FirebaseApplication('https://your_project_name.firebaseio.com/', None)

  # update data
  firebase_obj.put('/parant/','child', data)

  # fetch data
  result = firebase_obj.get('/parent/child', None)
  print (result)

[![image](https://user-images.githubusercontent.com/50515418/116424009-cd519480-a85e-11eb-943f-e566d49bad09.png)](https://github.com/imvickykumar999/Firebase-CRUD/blob/bdeb5b7a0b703b2f86719ee2da0d06505ee00ceb/main.py#L16)
