# defining the correct password
pwd=12345
#setting the number ofattempts
tries=5

#asking the user repeatedly for the password until the correct one is typed
while tries>0:
    guess=int(input('enter the password: '))
    if guess==pwd:
        print('correct password!')
        break
    else:
        tries=tries-1
        print('wrong, you have', tries,'attempts left')
        
# informing the user that the authoritiees have been alerted if the user reaches maximum attempts
if tries==0:
    print('you have reached maximum number of attempts. the authorities have been alerted')
    