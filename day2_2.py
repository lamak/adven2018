from datetime import datetime

fname = 'day2_1_data'

with open(fname) as f:
    source = f.readlines()

source = [x.strip() for x in source]
start = datetime.now()

for ids, temp in enumerate(source):
    for comp in source:
        if temp != comp and len(temp) == len(comp):
            counter, result = 0, ''
            for idx, ch in enumerate(temp):
                if ch != comp[idx]:
                    counter += 1
                else:
                    result += ch
            if counter == 1:
                print(temp, comp, result, datetime.now()-start)
    source.pop(ids)
