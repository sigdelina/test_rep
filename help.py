def text():
    word_list = []
    with open("text.txt", encoding = "utf-8") as f:
        lines = f.readlines()
        words = lines.split(" ")
        words = words.strip(" ,.?!;:""", "/t", "/n")
        word_list.append(words)
        print(word_list)
    
        

