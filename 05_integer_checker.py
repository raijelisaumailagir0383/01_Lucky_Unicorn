# Ask user for number
# Loop question sa that it repeats until valid number is entered
# Make code recyclable


# function goes here
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter an integer between {} and {}".format(low,high )

        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# main routine goes here

number = intcheck("Number: ", 1, 10)

