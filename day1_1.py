fname = 'day1_1_data' 

summ = 0

with open(fname) as f:
    for line in f:
        summ += int(line)

print(summ)
