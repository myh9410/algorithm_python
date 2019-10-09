"""
#재귀
numbers = [1,1,1,1,1]
target = 3
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:],target-numbers[0]) + solution(numbers[1:],target+numbers[0])
"""
#DFS
#재귀함수를 이용하여 DFS방식으로 풀이.
#                               (0,0) --> (idx,value)
#               (1,1)                           (1,-1)
#       (2,2)           (2,0)           (2,0)           (2,-2)
#  (3,3)    (3,1)   (3,1)   (3,-1)  (3,1)   (3,-1)  (3,-1)  (3,-3)
#DFS로 탐색하여 idx = 3이고 target = 1일때의 값 (3,1)을 찾아냄... 답 3개
# (0,0) (1,1) (2,2) (3,3) (3,1)
# 부모노드로 돌아가서 (2,0) (3,1) (3,-1)
# 루트노드로 돌아가서 (1,-1) (2,0) (3,1) (3,-1)
# 부모노드로 돌아가서 (2,-2) (3,-1) (3,-3) 순서로 탐색
answer = 0
numbers = [1,1,1]
target = 1
#N = 3
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])

DFS(0,numbers,target,0)
print(answer)