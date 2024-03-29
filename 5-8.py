ss = input("문자열 입력  ; ")

print("입력한 문자열", ss)

if ss.isupper() : #모든 문자열이 대문자이면 참
    print("소문자로 변경 : ", ss.lower())
if ss.islower() :
    print("대문자로 변경 : ", ss.upper())
