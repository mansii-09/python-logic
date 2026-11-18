n = int(input("Enter a number: "))

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)


#print prime number from 1 to 500
# for num in range(2,501):
#     is_prime = True

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num)

# 1. n = int(input(...))
# User pase maximum number input le chhe. Example: 10

# 2. for num in range(2, n + 1):
# 2 thi 10 sudhina darek number check karse.

# 3. is_prime = True
# Shuruaat ma number prime chhe evu mani laiye chhiye.

# 4. for i in range(2, int(num ** 0.5) + 1):
# Aa number ne 2 thi ena square root sudhina numbers vade divide kari ne check kare chhe.

# 5. if num % i == 0:
# Jo remainder 0 hoy, to number completely divide thay chhe.

# 6. is_prime = False
# Jo completely divide thay, to te prime nathi.

# 7. break
# Divisor mali jay pachhi inner loop bandh kari de chhe.

# 8. if is_prime:
# Jo number prime hoy, to print kare chhe.


#prime or not prime
# num = int(input("Enter a number: "))

# if num < 2:
#     print("Not prime")
# else:
#     is_prime = True

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime")
#     else:
#         print("Not prime")