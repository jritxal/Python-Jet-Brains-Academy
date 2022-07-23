# put your code here
num = -1
total_sum = 0
n = 0
stop = 55
while n != stop:
    num += 1
    total_sum += n
    n = int(input())
print(num)
print(total_sum)
print(round(total_sum / num))
