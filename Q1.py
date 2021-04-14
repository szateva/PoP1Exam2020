def func(L1, L2):
    if L1 == [] and L2 == []:
        return []
    else:
        return [(L1[0]+L2[0])/2] + func(L1[1:], L2[1:])

L1 = [1, 2, 3, 4, 5]
L2 = [2, 3, 4, 5, 6]

new = func(L1, L2)
print("the new lis it: ", new)