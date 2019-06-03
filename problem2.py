x = 227
y = 221
z = 220

largest = 0

if(x % 2 != 0):
    if (largest < x):
        largest = x
    if(y % 2 != 0):
        if (largest < x and x > y):
            largest = x
    if (z % 2 != 0):
        if (largest < x and x > z):
            largest = x

if(y % 2 != 0):
    if (largest < y):
        largest = y
    if(x % 2 != 0):
        if (largest < y and y > x):
            largest = y
    if (z % 2 != 0):
        if (largest < y and y > z):
            largest = y

if(z % 2 != 0):
    if (largest < z):
        largest = z
    if(x % 2 != 0):
        if (largest < z and z > x):
            largest = z
    if (y % 2 != 0):
        if (largest < z and z > y):
            largest = z

if(largest != 0):
    print ('Largest: ', largest)
else:
    print ('No odd numbers found')