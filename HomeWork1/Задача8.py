n = 3
m = 2
k = 4
if k > n * m:
    print("no")
else:
    if k % n == 0 or k % m == 0:
        print("yes")
    else:
        print("no")