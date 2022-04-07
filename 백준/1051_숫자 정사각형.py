# 백준 1051번. 숫자 정사각형
# https://www.acmicpc.net/problem/1051

# N : 직사각형의 세로
# M : 직사각형의 가로
# 꼭짓점에 쓰여 있는 수가 모두 같도록
# 출력: 정사각형의 넓이

N, M = map(int, input().split())

arr = []
for i in range(N):
  arr.append(list(input()))

n = min(N, M)   # 정답은 최대 n
answer = 1

while n>1:
  for i in range(N):
    for j in range(M):
      if i+n<=N and j+n<=M:
        # print(i, j, n)
        # print(arr[i][j], arr[i][j+n-1])
        # print(arr[i+n-1][j],arr[i+n-1][j+n-1])
        # print()
        if arr[i][j]==arr[i][j+n-1] and arr[i][j]==arr[i+n-1][j] and arr[i][j]==arr[i+n-1][j+n-1]:
          answer = n
          break
  if answer!=1:
    break
  n-=1

print(answer*answer)
