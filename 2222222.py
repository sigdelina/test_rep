s = []
t = 0
with open("freq1.txt", 'r', encoding = 'utf-8') as f:
    for line in f:
        word = line.split("|")
        l = word[1].split(" ")
        if l[1] == "союз":
            print(word[0])
        if "жен" in word[1]:
            s.append(word[0])
            t = t + float(word[2])
for i in range(len(s)):
    print(s[i]+',')
    print("summa", t)    

            
