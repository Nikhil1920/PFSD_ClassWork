f = open("test.txt", "xt")
f.write("Am happy today")
f.close()


for x in range(226):
    f = open("test{}.txt".format(x), "xt")
    f.write("Am happy today")
    f.close()
