import sys

number = int(sys.argv[1])

for i in range(1, number + 1):  # loop between 1 and number
    if number % i == 0:  # check if 'i' is a divisor of 'number'
        print(i, end=" ")
print()
