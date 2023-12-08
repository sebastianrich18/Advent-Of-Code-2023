
with open("day1/input.txt", 'r') as f:
    lines = f.readlines()

out = []
numberStrs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in lines:
    print(line.strip())
    nums = []
    for num in numberStrs:
        while num in line: # extract all number strings
            if num in line:
                nums.append((str(numberStrs.index(num) + 1), line.index(num)))
                print("found", num, "at", line.index(num))
                line = line.replace(num[1:-1], '-' * (len(num) - 2), 1)
        for char in line:
            if char.isnumeric():
                if (char, line.index(char)) not in nums:
                    nums.append((char, line.index(char))) # this doesnt work if there are multiple of the same number
                line = line.replace(char, '-', 1)
                
    nums.sort(key=lambda x: x[1])
    out.append(nums[0][0] + nums[-1][0])
    print(nums)
    print(line.strip(), (nums[0][0] + nums[-1][0]))
    print()

total = 0
for num in out:
    total += int(num)

print()
print(total)