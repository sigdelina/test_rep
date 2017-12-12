word = input()
word_list = []
word_list.append(word)
if word != '':
    word = input("add")
    word_list.append(word)
if word == "":
    print("no word")
with open("freq.txt", "r", encoding = "utf-8-sig") as file:
    for line in file:
        word_file= line.split("|")
        for word in word_list:
            if word == word_file:
                print(line)
            else:
                print("nein word")
            
