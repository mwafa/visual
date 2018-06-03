tebakan = 0
for k in range(5):
    i = 2**k
    data = [j for j in range(32) if (j//i)%2 == 1]
    print(data)
    a = input("ada disini?[Y/N]")
    tebakan = tebakan + i if a in ["y","Y"] else tebakan
print(tebakan)