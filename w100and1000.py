num = 100
sum = 0
count = 0
print("Armstrong numbers betweeen 100 and 1000")
while num <= 1000:
    que = num
    while que != 0:
        rem = que % 10
        sum = sum + (rem * rem * rem)
        que = int(que / 10)
    if sum == num:
        print(num)
        count += 1
    sum = 0
    num += 1
