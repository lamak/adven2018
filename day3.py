from datetime import datetime

fname = 'day3'

start = datetime.now()
with open(fname) as f:
    source = f.readlines()


class Box:
    def __init__(self, name: str, x: int, y: int, width: int, length: int):
        self.name = name
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def __str__(self):
        return self.name


def create_box_from_line(line_from):
    # #1249 @ 812,473: 28x15

    line_from = line_from.split(' ')
    name = line_from[0]
    y = int(line_from[2].strip(':').split(',')[0])
    x = int(line_from[2].strip(':').split(',')[1])
    length = int(line_from[3].split('x')[0])
    width = int(line_from[3].split('x')[1])

    return Box(name, x, y, width, length)


boxes = []
for line in source:
    boxes.append(create_box_from_line(line))

max_w, max_l = [], []
for box in boxes:
    max_w.append(box.x + box.width)
    max_l.append(box.y + box.length)

max_l = sorted(max_l, reverse=True)[0]
max_w = sorted(max_w, reverse=True)[0]

blank = []
for w in range(max_w):
    blank.append([])
    for l in range(max_l):
        blank[w].append(0)

for box in boxes:
    for x in range(box.width):
        for y in range(box.length):
            blank[box.x + x][box.y + y] += 1

counter = 0
for x, x_data in enumerate(blank):
    for y, y_data in enumerate(x_data):
        # print(x, y)
        if blank[x][y] >= 2:
            counter += 1

for box in boxes:
    box.temp = []
    for x in range(box.width):
        for y in range(box.length):
            box.temp.append(blank[box.x + x][box.y + y])
    if all([True if a == 1 else False for a in box.temp]):
        print(box.name, datetime.now() - start)
