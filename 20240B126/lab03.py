#int 사용시 소수점 안 나옴
#float 사용시 소수점까지 나옴

pound = float(input("파운드(1b)를 입력하세요 : "))
kg = pound * 0.453592
#print(pound, "파운드(1b)는", kg, "킬로그램(kg)입니다")
print("%d 파운드는 %.2f 킬로그램입니다" %(pound,kg))
