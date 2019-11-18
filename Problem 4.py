def palindrome():
    num1 = 1
    num2 = 1

    while num1 < 100 and num2 < 100:
        if num1 * num2 == 9009:
            print(num1, "and", num2)
            break
        else:
            num2 += 1
        if num2 == 100:
            num1 += 1
            num2 = 1

def find_if_palindrome(i):
    num = i
    temp = num
    rev= 0
    while num>0:
        dig = num%10
        rev = rev*10+dig
        num = num//10
    if temp==rev:
        return True
    else:
        return False
def find_max_palindrome():
    num1=1
    num2=1
    num3=1
    num2_count=0
    num1_count=0
    while num1 <100 and num2 <100 and num3<100:
        i= num1 * num2 * num3
        if find_if_palindrome(i):
            print("Palindrome:",num1*num2*num3,"from", num1,"and",num2,"and",num3)
            num2+=1
        else:
            num2+=1
        if num2 == 100:
            num1 += 1
            num2 = 1
            num3+=1
        if num1 == 100:
            num1=1
            num2+=1
            num3+=1
        if num3 == 100:
            num1+=1
            num2+=1
            num3=1
numbers=[]
def find_max_palindrome_3digits():
    num1=1
    num2=1
    while num1 <1000 and num2 <1000:
        i= num1 * num2
        if find_if_palindrome(i):
            print("Palindrome:",num1*num2,"from", num1,"and",num2)
            num2+=1

            numbers.append(i)

        else:
            num2+=1
        if num2 == 1000:
            num1 += 1
            num2 = 1

find_max_palindrome_3digits()
sorted_list = sorted(numbers)
print(sorted_list)
