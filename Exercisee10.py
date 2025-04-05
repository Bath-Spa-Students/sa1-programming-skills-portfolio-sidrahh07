# defining the function that checks if a given number is even or odd 
def check(number):
    if number%2==0:
        return "your number is even"
    else:
        return "your number is odd"

# defining the main function
def main():
    n=int(input('enter the number: '))
    ans= check(n)
    print(ans)

#calling the main function
main()
