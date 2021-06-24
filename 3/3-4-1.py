# 1이 될 때까지
import time

n, k = map(int, input().split())

start_time = time.time()

result = 0
while n >= k:
    a = n % k
    if a == 0:
        n //= k
        result += 1
    else:
        n -= a
        result += a
result += n - 1
print(result)

print(f"time: {time.time() - start_time}")
