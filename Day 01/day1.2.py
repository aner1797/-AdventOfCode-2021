tot = 0
newList=[]

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

for i in range(len(content_list)-1):
    tmp = [int(x) for x in content_list[i:i+3]]
    if len(tmp) == 3:
        newList.append(sum(tmp))

for i in range(len(newList)-1):
    if int(newList[i]) < int(newList[i+1]):
        tot+=1

print(tot)    