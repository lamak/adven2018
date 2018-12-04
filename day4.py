from datetime import datetime

fname = 'day4'

start = datetime.now()
with open(fname) as f:
    source = f.readlines()

source.sort()

events, dates, guard = [], [], None


class Event:
    def __init__(self, dt: datetime, guard, status):
        self.dt = dt
        self.guard = guard
        self.status = status


class Shift:
    def __init__(self, date, minute, guard, status):
        self.date = date
        self.sleep = []
        self.guard = guard
        self.status = status


for i in source:
    dt = datetime.strptime(i[1:17], "%Y-%m-%d %H:%M")
    if 'begins' in i:
        guard = i[19:].split(' ')[1]

    if 'wakes up' in i:
        status = True
        events.append(Event(dt, guard, status))

    elif 'falls asleep' in i:
        status = False
        events.append(Event(dt, guard, status))

# for e in events:
#     print(e.dt.date(), e.dt.hour, e.dt.minute, e.guard, e.status)

# for e in events:
