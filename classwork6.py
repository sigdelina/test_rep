f = open('lion.txt', 'r', encoding='utf-8-sig')
line = f.readline()
for line in f:
    for word in line:
        word = line.split(" ")
    print (len(line))
f.close()
#открывает файл и для каждой строчки для выходной строчки в формате цсв узнать сколько слов в строчке и какое первое слово
