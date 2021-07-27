# 프로그래머스 > 코딩테스트 연습 > 스택/큐 > 문제: 기능개발
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    # 먼저 배포되어야 하는 작업을 스택의 top이 되도록 함.
    progresses.reverse()
    speeds.reverse()
    
    answer = []
    
    # while문 한 번 반복은 하루가 지나감을 의미. (작업진도 스택이 비워질 때까지 반복)
    while progresses:
        # 작업진도 업데이트
        for idx, p in enumerate(progresses.copy()):
            progresses[idx] += speeds[idx]

        # 작업진도 확인 및 배포 (스택의 top부터 확인)
        n_release = 0
        for p in reversed(progresses):
            if p >= 100:
                progresses.pop()
                n_release += 1
            else:
                break
        if n_release:
            answer.append(n_release)
    
    return answer
