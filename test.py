def even_nums(nums):
    even_nums=[]
    for i in range(nums+1):
        if i % 2 == 0 and i != 0:
            even_nums.append(i)
    return even_nums

print(even_nums(50))