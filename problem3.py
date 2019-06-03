val = input("Enter n: ")
result = 0

for i in range(1, int(val) + 1):
    result += i

dCheck = (int(val) * (int(val) + 1)) / 2

if (result == dCheck):
    print("The nth triangular number is: ", result)

else:
    print ("The formula result and for loop result differs.")