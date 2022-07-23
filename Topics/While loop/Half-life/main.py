initial = int(input())
final = int(input())
n = 0
days_per_half = 12
while initial > final:
    initial //= 2
    n += 1
print(n * days_per_half)
