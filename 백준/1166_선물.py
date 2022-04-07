# 백준 1166번
# https://www.acmicpc.net/problem/1166

# 입력: N, L, W, H
# N = 정육면체 박스 개수
# L = 직육면체 박스 가로
# W = 직육면체 박스 세로
# H = 직육면체 박스 높이


N, L, W, H = map(int, input().split())

if N==1:
    print(min(L, W, H))  # A의 최대값

else:
  start, end = 0, max(L, W, H)
  for _ in range(100):
    mid = (start+end)/2
    num = (L//mid)*(W//mid)*(H//mid)
    if num >= N:
      start = mid
    else:
      end = mid

  print(end)
