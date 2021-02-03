import random
import string

capletter = string.ascii_uppercase
letters = string.ascii_lowercase
numbers = string.digits

for i in range(10):
    otp = (random.choice(capletter), random.choice(numbers),
           random.choice(letters), random.choice(numbers), random.choice(letters))
    out = "".join(otp)
    print(out)
