val = input("Enter the factorial number: ")
result = 1

for i in range(1, int(val) + 1):
    result *= i

print("Factorial of",val,"is: ", result)