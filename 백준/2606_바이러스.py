# 백준 2606번. 바이러스
# https://www.acmicpc.net/problem/2606

# 입력1: M = 컴퓨터 수
# 입력2: N = 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
# 입력3: N만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍

count = 0
def dfs(graph, v, visited):
  global count
  visited[v] = True
  #print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
      count += 1


M = int(input())
N = int(input())
graph = [[] for _ in range(M+1)]
for i in range(N):
  a, b = list(map(int, input().split()))
  graph[a].append(b)
  graph[b].append(a)

#print(graph)

visited = [False]*(M+1)
dfs(graph, 1, visited)
#print(visited)
print(count)
