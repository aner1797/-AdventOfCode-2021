gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]
finalGam = ""
finalEps = ""

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

for bin in content_list:
    for i in range(len(bin)):
        if int(bin[i]) == 0:
            gamma[i] -= 1
        if int(bin[i]) == 1:
            gamma[i] += 1 

for i in range(len(gamma)):
    if gamma[i] > 0:
        finalGam += "1"
        finalEps += "0"
    else:
        finalGam += "0"
        finalEps += "1"

print(int(finalGam, 2) * int(finalEps, 2))