# 공유기 설치
from sys import stdin

n, c = map(int, stdin.readline().split())
array = sorted([int(stdin.readline()) for _ in range(n)])

start, end, result = 1, array[-1] - array[0], 0
while start <= end:
    value, mid, count = array[0], (start + end) // 2, 1
    for i in range(1, n):
        if array[i] >= value + mid:
            count = count + 1
            if c <= count:
                break
            value = array[i]
    else:
        end = mid - 1
        continue
    start, result = mid + 1, mid

print(result)

"""
입력 예시
5 3
1
2
8
4
9

출력 예시
3
"""
