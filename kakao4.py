import re

queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
ans = []
for i in range(len(queries)):
    count = 0
    queries[i] = queries[i].replace("?","[a-z]") + "$"
    for j in range(len(words)):
        t = re.compile(queries[i])
        if t.search(words[j]) != None:
            count +=1
    ans.append(count)

print(ans)