tot = 0

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

for i in range(len(content_list)-1):
    if int(content_list[i]) < int(content_list[i+1]):
        tot+=1

print(tot)    