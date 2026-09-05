import sys

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



if len(user_numbers) <= 1:
    print("You did not entered enough numbers. The program will end! Try again!")
    sys.exit()



largestnumber = user_numbers[0]

for i in range(1,len(user_numbers)):

    if user_numbers[i] > largestnumber:
        largestnumber = user_numbers[i]
     

print(f"The list of numbers is : {user_numbers}")
print(f"Largest number is {largestnumber}")