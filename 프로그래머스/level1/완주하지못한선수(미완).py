# 1. 리스트 사용
# 정확성 통과, 효율성 실패
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for name in participant:
        if name not in completion:
            return name
        else:
            if participant.count(name) != completion.count(name):
                return name
