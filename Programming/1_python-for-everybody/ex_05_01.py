num = 0
total = 0.0

while True:
    user_input = input('Enter a number: ')

    # if user types "done" the script will exit the loop and print the results
    if user_input == 'done':
        break

    # try/ expect -> if input is invalid the loop starts again, no valies assigned
    try:
        val = float(user_input)
    except:
        print('Invalid input')
        continue

    # Adding the numbers for every loop
    num = num + 1
    total = total + val


# printing the results
print('Numbers:', num, 'Total:', total, 'Average:', total/num)
