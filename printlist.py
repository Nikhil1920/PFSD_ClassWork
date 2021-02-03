passenger_name = ["anirudh", "kishan", "goutham", "tejesh"]
train_num = [1918, 1920, 1922, 1924]
source = ["pune", "delhi", "chennai", "mumbai"]
destination = ["vijayawada", "madurai", "hyderabad", "vizag"]

for x in range(4):
    print('%s %d %s %s' %
          (passenger_name[x], train_num[x], source[x], destination[x]))
