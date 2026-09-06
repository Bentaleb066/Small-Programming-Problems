
user_numbers = []
print( "You will type more than one number and the largest number will be returned! When you are done entering numbers, type 'done'! ")

while True:
    try:
        user_input = input("Enter a number: ")

        if user_input.lower() == "done":
            break
        else: user_numbers.append(float(user_input))

    except ValueError as error:
            print(f"The input is invalid and cannot be converted to a float : {error}")



if len(user_numbers) < 1:
    print(f"The list of numbers is : {user_numbers}")
    print("You did not enter a number. The program will therefore end! Try again!")
    

elif len(user_numbers) == 1:
    print(f"The list of numbers is : {user_numbers}")
    print(f"The largest number is the only one you entered, which is {user_numbers[0]}")
    

else:

    largestnumber = user_numbers[0]

    for i in range(1,len(user_numbers)):

        if user_numbers[i] > largestnumber:
            largestnumber = user_numbers[i]
        

    print(f"The list of numbers is : {user_numbers}")
    print(f"Largest number is {largestnumber}")
    