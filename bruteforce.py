"""
1번 - 12345 / 12345              5단위
2번 - 21232425 / 21232425        8단위
3번 - 3311224455 / 3311224455    10단위
"""
num1 = [1,2,3,4,5]
num2 = [2,1,2,3,2,4,2,5]
num3 = [3,3,1,1,2,2,4,4,5,5]
count1,count2,count3 = 0,0,0
answers = [1,2,3,4,5]
answer = []

for i in range(len(answers)):
    if answers[i] == num1[i%len(num1)]:
        count1+=1
    if answers[i] == num2[i%len(num2)]:
        count2+=1
    if answers[i] == num3[i%len(num3)]:
        count3+=1

if max(count1,count2,count3) == count1:
    answer.append(1)
if max(count1,count2,count3) == count2:
    answer.append(2)
if max(count1,count2,count3) == count3:
    answer.append(3)

print(answer)