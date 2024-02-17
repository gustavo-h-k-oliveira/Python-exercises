print("------------------")
print("Fibonacci sequence")
print("------------------")

number = int(input("Insert a number to find out how many Fibonacci sequence numbers there are between 1 and it: "))
fibonacci_number = [1, 1, 0]

if (number < 0):
    print("Enter a number greater then zero.")
elif (number == 0):
    print("The only number in the Fibonacci sequence is zero.")
elif (number == 1):
    print("The numbers in the Fibonacci sequence are 0, 1 and 1.")
else:
    print("The Fibonacci sequence are: ")
    print(0)
    print(1)
    print(1)
    while (number >= fibonacci_number[2]):
        fibonacci_number[2] = fibonacci_number[0] + fibonacci_number[1]
        print(fibonacci_number[1])
        fibonacci_number[0] = fibonacci_number[1]
        fibonacci_number[1] = fibonacci_number[2]
        
