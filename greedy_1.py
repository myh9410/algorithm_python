n=5
lost = [2,4]
reserve = [5]
#뭘 틀렸는지 모르겠네 ㅅㅂ


def checker(n, lost, reserve):
    answer = n - len(lost)
    while (1):
        if lost[0] == reserve[0]:
            lost.remove(lost[0])
            reserve.remove(reserve[0])
        elif lost[0] > reserve[0]:
            if lost[0] - 1 == reserve[0]:
                answer += 1
                lost.remove(lost[0])
                reserve.remove(reserve[0])
            elif lost[0] + 1 == reserve[0]:
                answer += 1
                lost.remove(lost[0])
                reserve.remove(reserve[0])
            else:
                lost.remove(lost[0])
        elif lost[0] < reserve[0]:
            if lost[0] == reserve[0] - 1:
                answer += 1
                lost.remove(lost[0])
                reserve.remove(reserve[0])
            elif lost[0] == reserve[0] + 1:
                answer += 1
                lost.remove(lost[0])
                reserve.remove(reserve[0])
            else:
                lost.remove(lost[0])

        if len(lost) == 0:
            return answer
            break
        elif len(reserve) == 0:
            return answer
            break
        elif answer == n:
            return answer
            break


def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    if (set(lost) | set(reserve)) - (set(lost) & set(reserve)) == set(lost) | set(reserve):  # 교집합이 없음
        return checker(n, lost, reserve)
    elif (set(lost) | set(reserve)) - (set(lost) & set(reserve)) != set(lost) | set(reserve):
        temp = list(set(lost) & set(reserve))
        for i in range(len(temp)):
            lost.remove(temp[i])
            reserve.remove(temp[i])
            return checker(n, lost, reserve)

print(solution(n,lost,reserve))