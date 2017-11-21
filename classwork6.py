f = open ( filename, 'a', encoding = 'utf-8') #r - read w - write a - add
f.write(somestring)#режим синтаксиса, то, что записываем в файл, функция понимает только сторку
int, float -> str()
list -> ''.join
#windows and perevod(perenos) strok: \r\n, a ne \n
f.write (string1 + '\n' + string2 + '\n') #strings with perenos
#csv and tsv - formats tables
for line in f: #read file postrochno
    name, birth = line.split('\t')#razbit po tabulacii na stroki esli tablica v formate csv s kolonkami rojdenie i imya
f.close()
