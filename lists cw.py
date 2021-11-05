nums = [34, 56, 34, 26, 80, 57, 98, 100, 80, 64, 102, 300, 35, 6, 87, 88]
final = []
count = 0
index = 0

for index in range(len(nums)):
    if nums[index] < 80 or nums[index] > 100:
        final.append(nums[index])
        count += 1

print(f'Number of integers in range 80-100: {len(nums)-count}')

print(final)
