number_list = [9, 41, 12, 3, 74, 15]
smallest_seen = None

for number in number_list :
    if smallest_seen is None:
        smallest_seen = number
    if number < smallest_seen :
        smallest_seen = number

print('Smallest number:', smallest_seen)
