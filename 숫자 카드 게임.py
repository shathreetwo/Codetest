# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)
# 이 코드는 입력으로 주어진 2차원 리스트에서 '각 행의 가장 작은 수'들 중에서 가장 큰 수를 찾는 알고리즘입니다.
