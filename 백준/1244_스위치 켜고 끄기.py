# 백준 1244번
# https://www.acmicpc.net/problem/1244

# 입력1 = 스위치개수(100이하 자연수)
# 입력2 = 0 또는 1이 스위치개수만큼
# 입력3 = 학생 수(100이하 자연수)
# 입력4 = 성별과 받은 수
# 입력5 = 성별과 받은 수


def change(num):
  if switch[num] == 0:
    switch[num] = 1
  else:
    switch[num] = 0
  return

N = int(input())
switch = [-1] + list(map(int, input().split()))
M = int(input())

for _ in range(M):
  sex, num = map(int, input().split())
  # 남학생 - num의 배수 모두 change
  if sex == 1:
    i = 1
    while num * i <= N:
      change(num * i)
      i+=1
  # 여학생 - num을 중심으로 대칭을 이루는 최대범위 찾아서 change
  else:
    change(num)
    for i in range(1, N//2):
      if num-i>0 and num+i<N+1:
        if switch[num-i] == switch[num+i]:
          change(num-i)
          change(num+i)
        else:
          break

for i in range(1, len(switch)):
  print(switch[i], end=' ')
  if i%20==0:
    print()
