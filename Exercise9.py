#defining the hello function
def hello():
    print('Hello')

# defining the main function and calling the hello funtion inside it 
def main():
    hello()

#calling the main function if the file is being run directly and not imported to another file
if __name__== "__main__":
    main()
    