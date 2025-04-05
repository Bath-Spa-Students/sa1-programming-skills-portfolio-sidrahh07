# asking the person's information from the user
name=input('enter name ')
hometown= input('enter hometown ')
while True: #asking the age and making sure its a numeric value
 age= input('enter age ')
 if age.isdigit():
  break
 else:
  print('please try again and type a numeric value')

# storing the information in a dictionary
info={'name':name, 'hometown':hometown,'age':age}

# printing the information line by line and getting rid of the spaces using 'sep'
print('name: ',info['name'], '\nhometown: ', info['hometown'],'\nage: ', info['age'], sep='')
