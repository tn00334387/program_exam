

def Find_mul(num):
    if num % 3 == 0 or num % 5 == 0:
        return 1
    else:
        return 0

def Sum_of_mul(number):
    number_sum = 0
    for i in range(0,number):
        if Find_mul(i):
            number_sum += i
    return number_sum

print "The sum of these multiples is {}".format(Sum_of_mul(1000))


