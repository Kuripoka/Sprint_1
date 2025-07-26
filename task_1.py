timeline = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0
timeline = timeline.replace(' ', '').replace('h', 'h,').replace('m', 'm,').replace('s', 's,')
timeline = timeline.split(',')
empty_removed = []
for part in timeline:
    if part:
            empty_removed.append(part)
timeline = empty_removed
for i in range(len(timeline)):
    timeline_part = timeline[i]
    minutes = int(timeline_part[:-1])
    unit = timeline_part[-1]
    if unit == 'h':
            total_minutes += minutes * 60
    elif unit == 'm':
            total_minutes += minutes
    elif unit == 's':
            total_minutes += minutes / 60
print(total_minutes)