prime_list = []
devided_list = []
wholenumber_list = []


def isPrime(j):
    number = j
    counter = 0
    for i in range(1, number):
        if number % i == 0:
            counter += 1
            # print(i)
            # print(number)
    # print(number, "has this many")
    # print(counter)
    if counter > 1:
        # print(number, "is not prime")
        return False
    else:
        # print(number, "is prime")
        return True


def total_prime():
    orgNr = 200
    prime_counter = 0
    for j in range(1, orgNr + 1):
        if isPrime(j):
            prime_list.append(j)
            prime_counter += 1
            # print(j)
    print("Total Prime Numbers in", j, "is", prime_counter)
    # print(prime_list)


def make_list():
    myNumber = 13195
    for prime in prime_list:
        devided_number = myNumber / prime
        devided_list.append(devided_number)
    # print(devided_list)


def find_factor():
    for number in devided_list:
        if number % 1 == 0:
            wholenumber_list.append(number)
    print(wholenumber_list)

def largest_prime_factor(num, div=2):
    while div < num:
        if num % div == 0 and num/div > 1:
            num = num /div
            div = 2
        else:
            div = div + 1
    return num

print(largest_prime_factor(600851475143))
