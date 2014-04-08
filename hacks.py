__author__ = 'kw'
for x in range(10001, 20000):
    with open("~/smallfiles/" + str(x) + ".txt", "w+") as f:
        f.write(str(x) + ",1,2,3")
        f.close()