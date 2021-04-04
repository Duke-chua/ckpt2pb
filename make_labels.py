f = open('labels.txt', 'a')
for i in range(2):
    f.writelines(str(i)+"\n")

f.close()
