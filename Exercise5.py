# defining the dictionaries
notleap={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
leap={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

# getting the month name ans asking if it is a leap year
month=int(input('type a month number: '))
year=input('is the year a leap year? press y for yes and n for no: ')

#displaying the needed output to the user
if year.lower()=='y':
    print('there are', leap[month],  'days in the month')
else:
     print('there are', notleap[month],  'days in the month')
     