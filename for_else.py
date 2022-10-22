nums = [12,16,17,18,21,31]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print('not found')