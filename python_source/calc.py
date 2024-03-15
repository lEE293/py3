num1 = input("숫자 1 입력 :") #input함수는 문자열로 출력한다 
num2 = input("숫자 2 입력 :")
print("num1 =", num1, "num2 =", num2)

#input 함수로 입력받은 숫자는 문자열이므로  정수로 강제 형변환
num1 = int(num1)
num2 = int(num2)

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
