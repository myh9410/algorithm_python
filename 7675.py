import re
T = int(input())
for i in range(T):
    N = int(input())
    words = input()
    arr = re.split('\W',words)
    ans = []
    count = 0
    for word in arr:
        rest = word[1:]
        if word == '':
            ans.append(count)
            count = 0
        else:
            if len(word) == 1 and word.capitalize() == word and word.isalpha():
                count +=1
            elif len(word) > 1 and word.capitalize() == word and rest.lower() == rest and word.isalpha():
                count +=1
    print("#"+str(i+1)+' '+' '.join(map(str,ans)))


#my name is Hye Soo. my id is Rhs0266. what your id Bro?

"""
def trans():
    N = int(input())
    word = input().split()
    result = [0 for x in range(0,N)]
    n = 0
    for i in word :
        if 65 <= ord(i[0]) <= 90 :
            if len(i) == 1:
                result[n] += 1
            elif i[-1] == '?' or i[-1] == '!' or i[-1] == '.':
                i = list(i)
                i.pop()
                triger = 1
                for x in i[1:] :
                    if not(97<= ord(x)<= 122 or 0<= ord(x)<=9):
                        triger = 0
                if triger:
                    result[n] += 1
                n += 1
            else :
                triger = 1
                for x in i[1:] :
                    if not (97<= ord(x)<= 122 or 0<= ord(x)<=9):
                        triger = 0
                if triger:
                    result[n] += 1
 
        elif i[-1] == '?' or i[-1] == '!' or i[-1] == '.':
            n += 1
    return result
 
T = int(input())
for test_case in range(1, T + 1):
    result = trans()
    print(f'#{test_case}',end ='')
    for i in result:
        print(f' {i}',end='')
    print()
"""