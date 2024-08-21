import random
numbers=[]
result="my numbers: "
cnt=0
while cnt<6: #몇번 반복할지 모를때 while문 
    num=random.randint(1,6)
    if num not in numbers:
        numbers.append(num)
        result=result+f" {num}"
        cnt=cnt+1    
print(numbers)
