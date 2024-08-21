import random
guess = 0 			# while문이 한번은 실행되도록 guess를 0으로 초기화
count = 0			# 누적 합계에 사용하려 count는 0으로 초기화
answer= random.randint(1,100)	# 1~100사이 임의의 정수값을 생성하고 answer변수에 할당
while guess!=answer:		# guess와 answer이 같지 않으면 게임을 계속한다.
    guess=int(input("숫자입력"))	# 입력받은 값은 문자열이므로 정수형자료형으로 바꾸는 함수 int()사용
    count=count+1		# 맞추기 시도할 때마다 count 변수 1씩 증가
    
    if(guess>answer):		# answer값이 더 작으면 DOWN 출력
        print("DOWN")
    elif(guess<answer):		# answer값이 더 크면 UP 출력
        print("UP") 
print("정답!",count, "번 만에 맞추었어요!") #guess와 answer이 같으면 while의 조건이 거짓이 되어 게임 종료

