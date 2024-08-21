def sum(*numbers):
    sum_value=0
    for number in numbers:
        sum_value=sum_value+number
    return sum_value

result=sum(2**3,7)
print(result)