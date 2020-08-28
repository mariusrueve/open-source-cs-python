number_list = [9, 41, 12, 3, 74, 15]
largest_seen = None

for number in number_list :
    if largest_seen is None:
        largest_seen = number
    if number > largest_seen :
        largest_seen = number

print('Largest number:', largest_seen)
