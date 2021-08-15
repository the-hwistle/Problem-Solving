# 프로그래머스 > 코딩테스트 연습 > 위클리 챌린지 > 2주차. 상호평가
# 문제링크: https://programmers.co.kr/learn/courses/30/lessons/83201

# 점수를 학점으로 변환
def get_grade(scores):
    grade = ""
    for score in scores:
        if score>=90:
            grade+='A'
        elif score>=80:
            grade+='B'
        elif score>=70:
            grade+='C'
        elif score>=50:
            grade+='D'
        else:
            grade+='F'
    return grade


# 입력: 학생 수 x 학생 수 크기의 이중리스트 (점수)
# 출력: 학생 별 점수 리스트
def solution(scores):
    n = len(scores)    # 학생 수
    answer = [0]*n
    
    scores = list(map(list, zip(*scores)))      # 전치행렬
    
    # 평균 계산
    for idx, score in enumerate(scores):
        # 유일한 최고점 또는 유일한 최저점인 경우는 자기자신이 채점한 점수를 제외
        if (score[idx] == max(score) and score.count(max(score)) == 1) or (score[idx] == min(score) and score.count(min(score)) == 1):
            answer[idx] = (sum(score) - score[idx])/(n-1)
        else:
            answer[idx] = sum(score)/n
    
    answer = get_grade(answer)
    
    return answer
