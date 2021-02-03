import random
import string

capletter = string.ascii_uppercase
letters = string.ascii_lowercase
numbers = string.digits
mix = letters + numbers

for i in range(10):
    # otp = (random.choice(capletter), random.choice(numbers),
    #        random.choice(letters), random.choice(numbers), random.choice(letters))
    # out = "".join(otp)
    otp = "".join(random.choices(mix, k=4))
    out = random.choice(capletter) + otp
    print(out)
