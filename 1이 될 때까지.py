n, k = map(int, input().split())
result = 0

# N이 K이상이라면 K로 계속 나누기
while n >= k:
  # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
  while n % k != 0:
    n -= 1
    result += 1
  # K로 나누기
  n //= k  # n = n // k
  result += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
# 1이 될때까지 1씩 빼기
while n > 1:
  n -= 1
  result += 1

print(result)
