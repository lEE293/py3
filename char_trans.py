ss = input("문자열 입력 : ")

print("입력한 문자열 : ", ss) #ss에 입력을 하고 결과값으로 ss2를 생성
ss2= ""

for i in ss:
    if i.isupper() : #모든 문자열이 대문자이면 참
       ss2 += i.lower() #ss.lower으로 입력하지 말고 반복문일 때 i.lower로 입력
    else:
       ss2 += i.upper()

print("대소문자로 변경 : ", ss2) 
       
