phrases = "happy-birthday"
second = int(input())
temp = "______________"
answer =""
t = second%14   #나머지
s = second//14  #몫
#answer = temp[t:] + phrases[:t]

if s%2 == 0:
    answer = temp[t:] + phrases[:t]
elif s%2 == 1:
    answer = phrases[t:] + temp[:t]

print(answer)