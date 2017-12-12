Оценки: 1 контрольная задача, 1 часть - 5 баллов, 1 и 2 часть - 8 баллов, 3 части - 10 баллов.
Правила оформления (этикета программирования) - писать (легкий) код, эффективный, читабельный.
Пробелы - проставлять для повышения читабельности.
 
Задание:
1) открыть файл csv
2) (значение) уровня счастья в разных странах, только 2016 год
3) принт (страна, значение)
 
with open ('C:/Users/Aternius/Desktop/happiness-cantril-ladder.csv.csv', 'r', encoding='utf-8') as f:
    #for line in f:
    lines = f.readlines()
    for line in lines:
        #print(line)
        cells = line.split(',')
        #print(cells)
        if cells [2] == '2016':
            lines2016.append(cells)
user_country = input ('Your country: ')
found_answer = False
for line in lines2016:
    if line[0] == user_country:
        #print(line[3]) #альтернатива решения
        value = float(line[3].strip(';\n')) #можно либо -1, либо 3, ибо значение в строке под номером 3 (разделение по запятой), но оно также последнее
        print(value)
        found_answer = True #по сути тру и фолс работают как иф - елс
        break
if not found_answer:
    print("Sorry, I don't know.")
 
    #отсортировать по топу 10 самых счастливых\несчастливых стран
    #bl = [[число, "страна"], [число, "страна"], ]
    #[cells [3], cells [0]]
    #sorted (bl, reverse = True)
