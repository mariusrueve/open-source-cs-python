num = 0
total = 0.0

while True:
    user_input = input('Enter a number: ')

    if user_input == 'done' :
        break

    val = float(user_input)
    print(val)
    num = num + 1
    total = total + val

print('Done!')
print('Numbers:', num, 'Total:', total, 'Average:', total/num)
