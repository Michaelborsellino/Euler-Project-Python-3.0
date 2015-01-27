table=[[]]
for x in range(0,21):
    row =[]
    for i in range(0,21):
        if x == 0:
            row.append(1)
        elif i == 0:
            row.append(1)
        else:
            row.append(0)
    table.append(row)
del table[0]
'''
for d in table:
    print(d)
'''
for d in range(1,21):
    for y in range(1,21):
        table[d][y] = table[d-1][y] + table[d][y-1]
'''
for d in table:
    print(d)
'''
print(table[20][20])