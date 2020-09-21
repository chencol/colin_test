import math
import csv
import random
donation_dict = {}


def find_number(numbers, number, start=None, end=None):
    if start == None and end == None:
        start = 0
        end = len(numbers) - 1

    if start == end:
        # if not numbers[start]==number:
        #   return None
        return start
    else:
        if (end-start) == 1:
            n1 = numbers[start]
            n2 = numbers[end]
            if number > n1:
                return end
            return start
        else:
            index = math.floor((start + end)/2)
            reference = numbers[index]
            if reference == number:
                return index
            else:
                if number > reference:
                    start = index
                else:
                    end = index
                return find_number(numbers, number, start=start, end=end)


numbers = [5, 7, 10, 14, 20]
print(find_number(numbers, 6))

with open('donation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        name = row[0]
        amount = int(row[1])
        donation_dict[name] = amount

donation_dict = {k: v for k, v in sorted(
    donation_dict.items(), key=lambda item: item[1], reverse=True)}

accumulate_donation_dict = {}
accumlated_amount = 0

for k, v in donation_dict.items():
    accumlated_amount += v
    accumulate_donation_dict[accumlated_amount] = k

# Get a random donation amount

r = accumlated_amount * (random.random())
accumlated_amount_list = list(accumulate_donation_dict.keys())

print(accumulate_donation_dict)
print("Random amount is " + str(r))
print("Index is " + str(find_number(accumlated_amount_list, r)))
print("Value is " +
      str(accumlated_amount_list[find_number(accumlated_amount_list, r)]))
print("Corresponding donator is " + accumulate_donation_dict[accumlated_amount_list[find_number(
    accumlated_amount_list, r)]])
