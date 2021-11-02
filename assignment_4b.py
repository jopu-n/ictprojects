from datetime import timedelta

# File name: assignment_4b.py
# Author: Johannes Natunen
# Description: Asks the user for an input and does various functions related to said input

def check_int(user_input): # Checks if a given variable is an integer
    return isinstance(user_input, int)

def divisible_by_2_and_7(user_input): # Checks if a given variable is divisible by both 2 and 7.
    
    if check_int(user_input) == True: # Checking, if the variable is an integer     
        if user_input % 2 == 0 and user_input % 7 == 0:
            print("The given number is divisible by 2 and 7.")
        
        else:
            print("The given number is not divisible by both 2 and 7.")
    
    else:
        print("To execute this function, you must enter a number.")

def convert_to_time(secs): # Converts a given variable into days, minutes, hours and seconds.
    
    if check_int(secs) == True and secs >= 0: # Checking, if the variable is an integer       
        timedelta_string = str(timedelta(seconds = secs)) # Using timedelta to automatically convert 
        split_times = timedelta_string.split(":")         # from seconds, no need to calculate
        print("In time, your number is ", split_times[0], "Hours, ", split_times[1], "Minutes and ", split_times[2], "Seconds.")
    
    else:
        print("You must input a number, and it must be higher than 0.")

def palindromic_number(user_input): # Checks if a given variable (integer) is palindromic
    
    if check_int(user_input) == True: # Checking, if the variable is an integer    
        string_number = str(user_input) # Turning the integer into a string, so it is more
                                        # easily reversible
        if string_number == string_number[::-1]:
            print("The number is palindromic.")
        else:
            print("The number is not palindromic.")
    
    else:
        print("To execute this function, you must enter a number.")

def list_even_tribonacci(user_input): # Lists even tribonacci numbers lower than the given variable
    
    if check_int(user_input) == True:  # Checking, if the variable is an integer    
        
        trib1: 0 # Variables which store 
        trib2: 0 # Tribonacci numbers' values
        trib3: 1 # in the phases of the function
        
        while trib3 < user_input: # A loop until the Tribonacci number grows too large
            trib_temp = trib1 + trib2 + trib3 # trib_temp: a variable to 
            trib1 = trib2                     # store the sum temporarily
            trib2 = trib3
            trib3 = trib_temp
            if trib3 % 2 == 0:
                print(trib3)

            print("Printed all even Tribonacci numbers until", user_input)
    
    else:
        print("To execute this function, you must enter a number.")

def calculate_factorial(user_input): # Calculates the factorial of the given variable
    
    if check_int(user_input) == True and user_input > 0 and user_input <= 10:  # Checking, if the variable is an integer
        fact_sum = user_input # Storing the sum in a variable                  # and between values 1 and 10

        for i in range(user_input):
            fact_sum = fact_sum * (user_input - i)
        print("Factorial of ", user_input, " is ", fact_sum)

    else:
        print("To execute this function, you must enter a number with value of 1 to 10.")

def main(): 
    
    print("Welcome to The Program!")
    
    try:
        user_input = int(input("First, you have to give a number: "))

        choose_action = int(input("""Now, choose which function to execute: \n
                            1: Is the given number an integer or not? \n
                            2: Is the given number divisible by both numbers 2 and ? \n
                            3: How many days, hours, minutes and seconds the given number is. \n
                            4: Is the given number a palindromic number? \n
                            5: List all even Tribonacci numbers until the given number. \n
                            6: Calculate the factorial of the given number (under 10) \n
                            7: Exit the program. \n"""))
    except:
        print("Something went wrong. Restarting program...")
        main()
        quit()
    
    finally:
        if check_int(choose_action) == False or choose_action < 1 or choose_action > 7: # Checks for an invalid action
            print("Invalid action! Restarting program.")
            main()
        
        elif choose_action == 1:
            if check_int(user_input) == True:
                print("It's an integer!")
            else:
                print("No integers found. ")

        elif choose_action == 2:
            divisible_by_2_and_7(user_input)

        elif choose_action == 3: 
            convert_to_time(user_input)

        elif choose_action == 4: 
            palindromic_number(user_input)

        elif choose_action == 5:
            list_even_tribonacci(user_input)

        elif choose_action == 6:
            calculate_factorial(user_input)

        elif choose_action == 7:
            quit()

if __name__ == "__main__":
    main()