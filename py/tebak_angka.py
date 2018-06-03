tebakan = 0
for k in range(5):
    i = 2**k
    print([j for j in range(32) if (j//i)%2 == 1])
    tebakan = tebakan + i if input("ada disini?[Y/N]") in ["y","Y"] else tebakan
print(tebakan)