def min_max(*numbers):
    min_value=numbers[0]
    max_value=numbers[0]
    for number in numbers:
        if min_value>number:
            min_value=number
        if max_value<number:
            max_value=number
    return min_value,max_value

result=min_max(1,2,3,4,8,5,6,345)
print(result)
a,b=min_max(123,3412345,234,34,2345)
print(f"최솟값:{a} 최댓값:{b}")
