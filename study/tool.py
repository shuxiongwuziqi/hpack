def showByte(n):
    res = []
    for i in n:
        res.append(bin(i)[2:].zfill(8))
    return res
