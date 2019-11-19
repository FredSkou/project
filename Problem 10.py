#Er lavet, men tager for langt tid at regne ud for min computer. 



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
            #print(j)
    print("Total Prime Numbers in", j, "is", prime_counter-1)
    print(prime_list)
    print(sum(prime_list))

total_prime()