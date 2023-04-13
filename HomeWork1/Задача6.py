number = 303312
sum1 = 0
sum2 = 0
while(number > 1000):
    sum1 = sum1 + number % 10
    number = number // 10
while(number > 0):
    sum2 = sum2 + number % 10
    number = number // 10
if(sum1 == sum2):
    print("yes")
else:
    print("no")