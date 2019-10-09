record = ["RECEIVE abcd@naver.com", "RECEIVE zzkn@naver.com", "DELETE", "RECEIVE qwerty@naver.com", "SAVE", "SAVE", "DELETE", "RECEIVE QwerTY@naver.com", "SAVE"]
temp = [] #임시보관함
result = [] #영구보관함
#result = ["abcd@naver.com", "qwerty@naver.com", "QwerTY@naver.com"]
for i in record:
    if "RECEIVE" in i:
        r,id = i.split(" ")
        temp.append(id)
    elif "DELETE" in i:
        temp.remove(temp[-1])
    else: #save
        for i in temp:
            if i in result:
                pass
            else:
                result.append(i)

print(result)
