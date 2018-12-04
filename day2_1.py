fname = 'day2_1_data'
count2 = 0
count3 = 0

with open(fname) as f:
    source = f.readlines()

for line in source:
    two, three = 0, 0
    for ch in line:
        if line.count(ch) == 3:
            three = True
        elif line.count(ch) == 2:
            two = True
    count2 += two
    count3 += three

print(count2, count3, count2*count3)