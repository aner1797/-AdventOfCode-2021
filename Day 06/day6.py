my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split(",")

for i in range(0,80):
    tmp = []
    for x in range(len(content_list)):
        if content_list[x] == 0:
            tmp.append(8)
            content_list[x] = 7
        content_list[x] = int(content_list[x]) - 1
    content_list = content_list + tmp

print(len(content_list))

