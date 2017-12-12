m = []
for i in range(0, 1000):
    r = input()
    if r != '':
        m.append(r)
    else:
        break
s = []
t = 0
with open("freq.txt", encoding = 'utf-8') as f:
    lines = f.readlines()
    #for line in lines:
    #    words = line.split("|")
    #    if "союз" in words[1]:
    #        print(words[0])
    #for line in lines:
     #   words = line.split("|")
     #   if "жен" in words[1]:
      #      s.append(words[0])
      #      t = t + float(words[2])
    for line in lines:
        words = line.split("|")
        for i in range(0, len(m)):
            if m[i] in words[0]:
                print(words[1]+words[2])        
#for i in range(len(s)):
#    print(s[i]+',')
#print("summa", t)
   
   

            
