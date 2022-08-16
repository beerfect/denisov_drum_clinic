number = 9

print(f'{number=}')

combs = []

for i in range(2**number):
    result = "{0:#b}".format(i)[2:]
    needed_zeros = number - len(result)
    # print('0'*needed_zeros, result,sep='')
    comb = '0'*needed_zeros + result
    combs.append(comb)

unic_combs = []

array = []

for comb in combs:
    # print(comb)
    this_is_unic_comb = True
    for unic_comb in unic_combs:
        if comb in unic_comb*2:
            this_is_unic_comb = False

    if this_is_unic_comb:
        unic_combs.append(comb)

for unic_comb in unic_combs:
    print(unic_comb[::-1])
    array.append(unic_comb[::-1])

# print(array)
del array[0]
del array[-1]
# print('group_',number, ' = ', array, sep='')
