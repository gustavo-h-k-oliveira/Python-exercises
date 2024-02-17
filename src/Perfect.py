print("---------------")
print("Perfect numbers")
print("---------------")

number = int(input("Insert a number to find out how many perfect numbers there are between 1 and it: "))
x = 1
sum = 0
all_numbers = []

while (x <= number):
    for i in range(1, x + 1):
        if i != x and (x % i == 0):
            # print(i)
            sum = sum + i

    # print(sum)
    # print(type(sum))

    if (sum == x):
        print("The number", x, "is a perfect number!")
        all_numbers.append(x)

    # else:
    #     print("The number", x, "isn't a perfect number!")
    
    sum = 0
    x += 1

print("The perfect numbers are:", all_numbers)