# Ask user for number
# Loop question sa that it repeats until valid number is entered
# Make code recyclable

# function goes here
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter an integer between {} and {}".format(low,high )

        try:
            response = int(input("Enter an integer between {} and {}: ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# main routine goes here

valid = False
while not valid:
    error = "Whoops! Please enter an integer between 1 and 10: "))

    try:
        response = int (input("Enter an ineteger between 1 and 10: "))

