'''
for i in range(0, 3, 1):
    for k in range(0, 2, 1):
        print("난생처음은 쉽습니다. (i값은 %d, k값은 %d)" % (i, k))

'''
#k = 2
for k in range(2, 10, 1):
    print("%d 단 :", % k, end='')
    for i in range(1, 10, 1):
        print("%d * %d = %2d" % (k, i, k*i),  end = '\t')

