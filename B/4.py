# 투 포인터
m, data = 5, [1, 2, 3, 2, 5]
start, end, difference, count = 0, 0, m - data[0], 0
while start < len(data) > end:
    if difference == 0:
        difference, start, count = difference + data[start], start + 1, count + 1
    elif difference < 0:
        difference, start = difference + data[start], start + 1
    elif difference > 0:
        end += 1
        difference -= data[end]
print(count)
