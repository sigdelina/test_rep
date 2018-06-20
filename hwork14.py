def read_text():
    elements = '.?!'
    text = []
    with open("hemi.txt", "r", encoding = "utf-8") as file:
        for lines in file:
            lines = lines.split(elements)
            text.append(lines)
    return text

def main():
    text = read_text()оалвдоыдлаовылдаовыдлаофвлдоафдовалофд
    print(text)
    
main()
