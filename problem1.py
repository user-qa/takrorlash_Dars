# 1. Ushbu list ichida for ishlatmasdan iterator va while orqali aylanib juft sonlarni yig'indisni toping
#       nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]


# Iterator orqali yechim

nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]
nums = iter(nums)
total = 0
try:
    while True:
        this_num = next(nums)
        if this_num%2 == 0:
            total += this_num
except:
    pass

print(total)

#List Comprehension orqali yechim

numbers = [12, 34, 5, 3, 2, 423, 2, 23, 44]
print(sum([i for i in numbers if i%2==0]))