import random
result='my_number:'

for i in range(10): #0~5까지 6번 반복실행
    num=random.randint(1,500)
    result=f"{i}:{num}"
    if 234 == num:
        print("당첨")
    else:
        print(".")
    



