sticker = [12,12,12,12,12]

def solution(sticker):
    d = [0] * len(sticker)
    d[0] = sticker[0]
    d[1] = sticker[1]
    for i in range(len(sticker)):
        d[i] = max(d[i - 1], sticker[i] + d[i - 2])

    answer = d[len(sticker) - 1]
    return answer