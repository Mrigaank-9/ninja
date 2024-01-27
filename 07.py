def addBinaryString(a, b, n, m):

    # Write your code here.

    na = len(a) -1

    nb = len(b) - 1

    aa = 0

    bb = 0

    for i in a:

        i = int(i)

        aa += i*(2**na)

        na -= 1

    for j in b:

        j = int(j)

        bb += j*(2**nb)

        nb -= 1

    return bin(aa + bb)[2:]

    pass