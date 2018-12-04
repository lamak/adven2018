fname = 'day1_1_data'

target, summ, result = [], 0, None

with open(fname) as f:
    source = f.readlines()

while result is None:
    for line in source:
        summ += int(line)
        if summ in target:
            result = summ
            break
        target.append(summ)

print(result)