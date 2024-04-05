for k in range(2, 10, 1) :
    print("%d 단 :" % k, end='')
    for i in range(1, 10, 1) :
        print("%d * %d = %2d" % (k, i, k*i),  end = '\t')
    print() #바깥쪽 for 문(카운터 변수 k인 for문)에서 실행
