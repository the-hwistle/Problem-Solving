# 프로그래머스 > 코딩테스트 연습 > 위클리 챌린지 > 3주차. 퍼즐 조각 채우기
# 문제링크: https://programmers.co.kr/learn/courses/30/lessons/84021

def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False

# 입력: 게임보드의 상태, 퍼즐조각의 상태 (정사각모양)
# 출력: 총 몇칸을 채울 수 있는지
def solution(game_board, table):
    answer = -1
    
    n = len(game_board)
    
    graph = []
    for i in range(n):
        graph.append(table[i])
    print(graph)
    
    
    
    return answer
