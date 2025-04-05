# defining the list of names
namelist=["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]

# asking the user to input the name
name=input('enter the name to search for: ').capitalize()

# searching for the name in the list of names
if name in namelist:
    print('name was found') #executes this if name was found
else:
    print('name was not found') #executes this if name was not found
    