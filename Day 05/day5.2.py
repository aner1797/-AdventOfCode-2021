my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

diagram = []
for x in range(0,1000):
    tmp = []
    for x in range(0,1000):
        tmp.append(0)
    diagram.append(tmp)
    
for cord in content_list:
    front, back = cord.split('->')
    x1, y1 = front.split(',')
    x1, y1 = int(x1), int(y1)
    x2, y2 = back.split(',')
    x2, y2 = int(x2), int(y2)

    if x1 == x2:
        tmp = abs(y1-y2)+1
        for x in range(0,tmp):
            if y1<y2:
                diagram[y1+x][x1] += 1
            else:
                diagram[y2+x][x1]  += 1
    elif y1 == y2:
        tmp = abs(x1-x2)+1
        for x in range(0,tmp):
            if x1<x2:
                diagram[y1][x1+x] += 1
            else:
                diagram[y1][x2+x]  += 1
    else:
        tmp = abs(x1-x2)+1
        for x in range(0,tmp):
            tmpX1, tmpX2, tmpY1, tmpY2 = x1, x2, y1, y2
            if tmpX1<tmpX2:
                tmpX1 += x
            else:
                tmpX1 -= x
            if tmpY1<tmpY2:
                tmpY1 += x
            else:
                tmpY1 -= x
            
            diagram[tmpY1][tmpX1]  += 1


count = 0
for x in diagram:
    for y in x:
        if y >= 2:
            count += 1

print(count)