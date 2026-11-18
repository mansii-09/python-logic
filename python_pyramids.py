# 1. Right-Angled Star Triangle  or left
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6):
    print("* " *i)

print("*"*50)

# 2. Right-Aligned Star Triangle
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range(1,6):
    print("  " *(6-i),"* " *i)    #"  " 2space

print("*"*50)

# 3. Centered Star Pyramid
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

for i in range(1,6):
    print(" " *(6-i), "* " * i)

print("*"*50)

# 4. Inverted Right Triangle
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5,0,-1):
    print("* " *i)

print("*" *50)

# 5. Inverted Centered Pyramid
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

for i in range(5,0,-1):
    print(" " *(5-i), "* " * i)

print("*" *50)

# 7. Hollow Right Triangle
# *
# * *
# *   *
# *     *
# * * * * *

for i in range(1, 6):
    if i == 1:
        print("*")
    elif i == 5:
        print("* " *5)
    else:
        print("*" + " " *(2*i - 3) + "*")


print("*"*50)

# 8. Hollow Centered Pyramid
#     *
#    * *
#   *   *
#  *     *
# *********

for i in range(1, 6):
    if i == 1:
        print(" " * (6 - i + 1) + "*")
    elif i == 5:
        print(" " ,"*" * 9)
    else:
        print(" " * (6 - i + 1) + "*" + " " * (2 * i - 3) + "*")
    


print("*"*50)
# 9. Hollow Inverted Pyramid
# *********
#  *     *
#   *   *
#    * *
#     *

for i in range(5, 0, -1):
    if i == 5:
        print(" " + "*" * 9)
    elif i == 1:
        print(" " * 5 + "*")
    else:
        print(" " * (6-i) + "*" + " " * (2*i-3) + "*")


print("*"*50)
# 10. Hollow Inverted Right Triangle
# * * * * *
# *     *
# *   *
# * *
# *
for i in range(5, 0, -1):
    if i == 5:
        print("* " * 5)
    elif i == 1:
        print("*")
    else:
        print("*" + " " * (2*i - 3) + "*")

print("*"*50)

# 11. Solid Star Square
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(5):
    print("* " *5)

print("*" *50)

# 12. Hollow Star Square
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

for i in range(5):
    if i == 0 or i == 4:
        print("* " * 5)
    else:
        print("*       *")

print("*" *50)

# 13. Solid Star Rectangle
# * * * * * *
# * * * * * *
# * * * * * *

for i in range(3):
    print("* " *6)


print("*" *50)

# 14. Hollow Star Rectangle
# * * * * * *
# *         *
# *         *
# * * * * * *

for i in range(4):
    if i == 0 or i == 3:
        print("* " * 6)
    else:
        print("*         *")

print("*" *50)

# 15. Half Diamond
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(1, 6):
    print("* " * i)

for i in range(4, 0, -1):
    print("* " * i)


print("*" *50)


# 16. Full Diamond
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

for i in range(1,6):
    print(" " *(6-i), "* " *i)

for i in range(4,0,-1):
    print(" "*(6-i), "* " *i)

print("*" *50)

# 17. Hollow Diamond
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

for i in range(1, 6):
    print(" " * (6-i), end="")
    print("*", end="")
    if i > 1:
        print(" " * (2*i-3) + "*", end="")
    print()

for i in range(4, 0, -1):
    print(" " * (6-i), end="")
    print("*", end="")
    if i > 1:
        print(" " * (2*i-3) + "*", end="")
    print()

print("*" *50)
# 18. Hourglass Star Pattern
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

for i in range(5,0,-1):
    print(" " *(5-i),"* " *i)
for i in range(2,6):
    print(" " *(5-i),"* " *i)

print("*" *50)
# 19. Butterfly Star Pattern
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

for i in range(1,6):
    print("* " *i +"  " *(2 * (5-i))+"* " *i)    #"* " *i--> banne(2) side starts banavse
                                                 # + karsu to j proper aavse comma(,) thi nai thay

for i in range(4,0,-1):
    print("* " *i +"  " *(2 * (5-i))+"* " *i)

print("*" *50)

# 21. X-Shaped Star Pattern
# *       *
#   *   *
#     *
#   *   *
# *       *

print("*"*50)
# 22. Plus-Shaped Star Pattern
#     *
#     *
# * * * * *
#     *
#     *

print("*"*50)

# 24. Staircase Star Pattern
# *
#  *
#   *
#    *
#     *

for i in range(5):
    print(" " *i , "*")

print("*" *50)

# 27. Centered Half Pyramid
#     *
#    ***
#   *****
#  *******
# *********

for i in range(1,6):
    print(" " * (6 - i) + "*" * (2 * i - 1))

print("*" *50)
# 28. Reverse Centered Half Pyramid
# *********
#  *******
#   *****
#    ***
#     *

for i in range(5,0,-1):
    print(" " * (6 - i) + "*" * (2 * i - 1))

print("*" *50)
# 32. Alternating Star Triangle
# *
# + + 
# * * *
# + + + +
# * * * * *

for i in range(1,6):
    if i % 2 != 0:
        print("*" * i)
    else:
        print("+" *  i)
    
print("*" *50)
# 33. Two-Sided Star Pyramid
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *

for i in range(1,6):
    print("* " *i +"  " *(2 * (5-i))+"* " *i)

print("*" *50)

# 38. Multi-Level Pyramid
#   *
#  ***
# *****
#    *
#   ***
#  *****
# *******
#     *
#    ***
#   *****
#  *******
# *********
for i in range(1,4):
    for j in range(1, i + 3):
        print(" " * (6 - j) + "*" *(2 * j -1))

print("*" *50)

# 39. Multi-Level Inverted Pyramid
# *********
#  *******
#   *****
#    ***
#     *
# *******
#  *****
#   ***
#    *
# *****
#  ***
#   *

for i in range(5, 2, -1):
    for j in range(i, 0, -1):
        print(" " * (5 - j) + "*" * (2 * j - 1))

print("*" *50)

# 40. Hollow Double Pyramid
#     *
#    * *
#   *   *
#  *     *
# *       *


print("*" *50)

# 42. Hollow Staircase
# *
# **
# * *
# *  *
# *   *

for i in range(1,6):
    print("*" + " " *(i- 2) + "*" * ( i > 1) )

print("*" *50)
# 44. Pyramid with Base
#     *
#    * *
#   *   *
#  *     *
# *********
print("*" *50)
# 46. Alternating number pyramid
# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1

for i in range(1,6):
    for j in range(1, i + 1):
        print(j % 2, end = " ")
    print()

print("*" *50)

# 47. Hollow number diamond
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(1,6):
    for j in range(i):
        print(i, end = " ")
    print()

print("*" *50)
# 48. Number X pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

print("*" *50)

# 49. Number plus pattern
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(5,0,-1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

print("*" *50)

# 50. Number arrow
#     1
#    121
#   12321
#  1234321
# 123454321

for i in range(1,6):
    print(" " * (6 - i), end = "")

    for j in range(1 , i + 1):
        print(j, end = "")

    for j in range(i-1, 0,-1):
        print(j, end="")

    print()

print("*" *50)
# 111. Repeated letter triangle
# A
# B B
# C C C
# D D D D
# E E E E E

for i in range(65,70):
    for j in range(65, i + 1):
        print(chr(i), end = " ")
    print()

print("*" *50)

# 112. Increasing alphabet triangle
# A
# A B
# A B C
# A B C D
# A B C D E

for i in range(65,70):
    for j in range(65,i + 1):
        print(chr(j), end = " ")
    print()

print("*" *50)

# 113. Decreasing alphabet triangle
# A B C D E
# A B C D
# A B C
# A B
# A

for i in range(5, 0, -1):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()


print("*" *50)
# 114. Centered alphabet pyramid
#     A
#    AB
#   ABC
#  ABCD
# ABCDE

for i in range(1,6):
    print(" " *(6-i), end = "")

    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()

print("*" *50)

# 155. Checkerboard pattern
#     1
#    222
#   33333
#  4444444
# 555555555

for i in range(1,6):
    print(" " *(6-i), end= "")
    print(str(i) * ( 2 * i - 1))