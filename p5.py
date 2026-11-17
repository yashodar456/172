num =int(input("Enter a number:"))
for i in  range(1, 21):
    print(num, "x", i, "=", num * i)

num = "i"
for i in range(1, 21):
    print(i)
total = 0

for i in range(1,11):
    total = total + i
    print("Sum =", total)
    num = 0

    for i in range(1, 51):
        if i % 2 == 0:
            print(i, end=" ")
        num = 1
    while num < 11:
        print(num, end=" ")
        num += 1
        



    