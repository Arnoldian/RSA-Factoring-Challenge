#!/usr/bin/python3

def factorize_v1(num):
    flag = 0
    for i in range(2, int(num / 2) + 1, 1):
        if num % i == 0:
            print("{:d}={}*{}".format(num, num // i, i))
            flag = 1
            break
    if flag == 0:
        print("{:d}={}*{}".format(num, num, 1))

def factorize_v2():
    with open(input("Enter the file name: ")) as f:
        for number in f:
            num = int(number)
            factorize_v1(num)

# To call the first function
num = 100
factorize_v1(num)

# To call the second function
factorize_v2()

