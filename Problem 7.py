


def isPrime(p):
    number = p
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
    for p in range(1, orgNr + 1):
        if isPrime(p):
            #prime_list.append(p)
            prime_counter += 1
            # print(j)
    print("Total Prime Numbers in", p, "is", prime_counter)
    # print(prime_list)

total_prime()