# (1)^3 + (5)^3 + (3)^3  = 153

num = int(input("Enter a number: "))
original = num
sum = 0

while num > 0:
    r = num % 10
    sum = sum +(r*r*r)
    num = int(num/10)

if sum == original:
    print("Your num is an armstrong..", sum)
else:
    print("Your num is not an armstrong..", sum)


# find armstrong number only 1 to 1000.

for i in range(1, 1001):
    num = i
    original = num
    sum = 0

    while num > 0:
        r = num % 10
        sum = sum + (r * r * r)
        num = int(num / 10)

    if sum == original:
        print(original)

# Include 1 to 9
for i in range(1, 1001):
    num = i
    original = num
    power = len(str(i))      # change 1: digits ni count
    sum = 0

    while num > 0:
        r = num % 10
        sum = sum + (r ** power)   # change 2: cube ni jagya e power
        num = int(num / 10)

    if sum == original:
        print(original)