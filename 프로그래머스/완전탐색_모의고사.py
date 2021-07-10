# [프로그래머스]
# 코딩테스트 연습 > 완전탐색 > 문제: 모의고사

def solution(answers):
    supoja1 = [1,2,3,4,5]           # 5
    supoja2 = [2,1,2,3,2,4,2,5]     # 8
    supoja3 = [3,3,1,1,2,2,4,4,5,5] # 10
    
    N = len(answers)
    score1, score2, score3 = 0, 0, 0
    
	  for i in range(N):
        answer = answers[i]
        if supoja1[i % 5] == answer:
            score1 += 1
        if supoja2[i % 8] == answer:
            score2 += 1
        if supoja3[i % 10] == answer:
            score3 += 1
            
    # 최댓값 찾기
    score = max(score1, score2, score3)
		# 최댓값의 점수를 가진 인덱스 모두 찾기
    answer = [idx+1 for idx, v in enumerate([score1, score2, score3]) if v == score]
    
    return answer
