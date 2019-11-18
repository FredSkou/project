def squared():
    total = 0
    for number in range(1, 101):
        number = number * number
        total += number
        print(number)

    print("Total for squared:", total)
    return total


def sum():
    new_number = 0
    n = 0
    while n < 10:
        for number in range(1,101):
            new_number += number
            n += 1
    total_sum = new_number ** 2
    print("Total sum:", total_sum)
    return total_sum




squared()
sum()
print("Difference is:", squared() - sum())
