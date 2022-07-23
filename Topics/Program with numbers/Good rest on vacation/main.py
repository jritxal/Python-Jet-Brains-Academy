# put your python code here
duration = int(input())
food_per_day = int(input())
flight = int(input())
cost_per_night = int(input())

print(food_per_day * duration + flight + flight + cost_per_night * (duration - 1))
