n = 0
initial_deposit = int(input())
max_refund = 700_000
increase_per_year = 1.071
while initial_deposit < max_refund:
    initial_deposit *= increase_per_year
    n += 1
print(n)
