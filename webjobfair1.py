goods = [5,3,7]
boxes = [3,7,6]

goods.sort(reverse=True)
boxes.sort(reverse=True)
ans = 0
while True:
    if boxes[0] >= goods[0]:
        boxes.remove(boxes[0])
        goods.remove(goods[0])
        ans+=1
    else:
        goods.remove(goods[0])
    if len(goods) == 0:
        break
    elif len(boxes) == 0:
        break

print(ans)

#그리디