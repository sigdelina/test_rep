from flask import Flask
import datetime
from flask import url_for, render_template, request, redirect, jsonify
import json
from json2html import *

app = Flask(__name__)

def create_File():
    row = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'
    with open('results.csv', 'w', encoding='utf-8') as file:
        file.write(row % ("имя", "возраст", "родной язык", 'родной город',
                          "пол", "уровень образования", "вопрос 1", "ворпос 2", "ворпос 3"))
    return

create_File()

@app.route('/')
def general():
    urls = {'Главная страница с опросом': url_for('general'),
            'Все ответов в формате json': url_for('jsonel'),
            'Статистика': url_for('stat')}
    if request.args:
        name = request.args['name']
        age = request.args['age']
        lang = request.args['lang']
        gender = request.args['gender']
        city = request.args['city']
        study = request.args['study']
        quest_1 = request.args['quest_1']
        quest_2 = request.args['quest_2']
        quest_3 = request.args['quest_3']
        row = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'
        with open('results.csv', 'a+', encoding='utf-8') as file:
            file.write(row % (name, age, lang, city, gender, study, quest_1, quest_2, quest_3))
        return render_template('answer.html', name=name, age=age, lang=lang, city=city,
                               gender=gender, study=study, quest_1=quest_1, quest_2=quest_2, quest_3=quest_3, urls=urls)
    return render_template('question.html')


@app.route('/json')
def jsonel():
    fin = []
    with open("results.csv", 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            line = line.split('\t')
            d = {"name": line[0], 'age': line[1], "lang": line[2], "city": line[3],
                 "gender": line[4], 'study': line[5], 'quest_1': line[6],
                 'quest_2': line[7],
                 "quest_3": line[8].replace('\n', '')}
            fin.append(d)
    json_string = json.dumps(fin[1:], ensure_ascii=False)
    json_obj_in_html = json2html.convert(json={"data": json_string})
    return render_template('json.html', json_obj_in_html=json_obj_in_html)

@app.route('/stats')
def stat():
    with open('resalts.csv') as file:
        filereader = csv.reader(csvfile, delimiter=';', quotechar='|')

if __name__ == '__main__':
    print(dictinf)
    app.run(debug=True)

#
