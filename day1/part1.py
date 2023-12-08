
with open("day1/input.txt", 'r') as f:
    lines = f.readlines()

out = []

for line in lines:
    nums = []
    for char in line:
        if char.isnumeric():
            nums.append(char)
    out.append(nums[0] + nums[-1])
    

total = 0
for num in out:
    total += int(num)

print(total)