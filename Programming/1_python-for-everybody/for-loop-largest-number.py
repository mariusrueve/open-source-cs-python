number_list = [9, 41, 12, 3, 74, 15]
largest_seen = int()

for number in number_list :
    if number > largest_seen :
        largest_seen = number

print('Largest number:', largest_seen)
