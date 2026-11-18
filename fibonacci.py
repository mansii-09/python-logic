n = int(input("Enter number: "))

a = 0
b = 1
i = 0

while i < n :
    print(a)
    c = a + b
    a = b 
    b = c
    i = i + 1

# use python tuple assignment   a, b = b, a + b  c variable ni jarur nathi aa rite pn kari shakay