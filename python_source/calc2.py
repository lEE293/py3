#한번에 여러 값을 입력 받는다 : split()  함수 -> 문자열을 특정문자를 기준으로 나눈다 
num1, op, num2 = input("숫자 1과 숫자2를 동시에 입력[100, 200]: "),split()

print("num1 = ", num1,"op =", op, "num2 = ", num2)
print("num1 = %s, op = %s, num2 = %s", op, num1, num2)

#input  함수로 입력받은 숫자는 문자열이므로 정수로 강제 형변환
num1 = input(num1)
num2 = input(num2)

#num1, num2를 문자열로 정수로 변환하였으므로 +는 덧셈 계산이 된다 
result = num1 + num2
print(num1, " + ", num2 ," = ", result)

result = num1 - num2
print(num1, " - ", num2 ," = ", result)

#문자 : 서식 지정자 -> 출력시 변수나 값으로 대체되는 기능
result = num1 * num2
print("%d * %d = %d" % (num1, num2, result))

result = num1 / num2
print("%d / %d = %d" % (num1, num2, result))
