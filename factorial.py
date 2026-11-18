# Example: 4! = 1 × 2 × 3 × 4 = 24

num = int(input("Enter number: "))

fact = 1
i = 1

while i <= num:
    fact = fact * i
    i = i + 1

print("Factorial=", fact)

