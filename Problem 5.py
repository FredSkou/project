list = []


def smallest_number():
    start_nr = 2520
    for divided_nr in range(1, 10):
        new_number = start_nr / divided_nr
        divided_nr += 1
        print(start_nr, "devided by:", divided_nr, "equalt", new_number)


def largest_number():
    number = 1
    max_number=2
    while number < max_number:
        number += 1
        if number % 2 == 0:
            print(number)


sorted_list = sorted(list)

# smallest_number()
largest_number()
