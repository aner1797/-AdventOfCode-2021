my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split(",")

def fuel(to, crabs):
    count = 0
    for x in crabs:
        tmp = abs(int(x)-int(to))
        count += tmp*(tmp+1)/2
    return count

tmp = []
for i in range(int(max(content_list))):
    tmp.append(fuel(i, content_list))

tmp.sort()
print(tmp[0])