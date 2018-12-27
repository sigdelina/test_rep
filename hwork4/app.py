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
            'Статистика': url_for('stat'),
            'Поиск': url_for('searching')}
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
    json_string = json.dumps(fin[1:], ensure_ascii=False, indent=4)
    json_date = json.loads(json_string)
    with open('json_info.json', 'w', encoding='utf-8') as f:
        json.dump(json_date, f, ensure_ascii=False, indent=4)
    #final = json2html.convert(json={"data": json_date})
    #json_obj_in_html = json2html.convert(json= json_string)
    return render_template('json.html', json_date=json_date)
    #return jsonify(json_date)

@app.route('/search')
def searching():
   # urls = {'Главная страница с опросом': url_for('general'),
   #         'Все ответов в формате json': url_for('jsonel'),
   #         'Статистика': url_for('stat')}
    if request.args:
        studying = request.args['studying']
        word = request.args['word']
        return render_template('resulting.html',studying=studying, word=word)
    return render_template('items search.html')

@app.route('/stats')
def stat():
    urls = {'Главная страница с опросом': url_for('general'),
            'Все ответов в формате json': url_for('jsonel')}
    rus_ked = []
    nrus_ked = []
    rus_keda = []
    nrus_keda = []
    rus_krvk = []
    nrus_krvk = []
    rus_krvka = []
    nrus_krvka = []
    rus_tpk = []
    nrus_tpk = []
    rus_tpka = []
    nrus_tpka = []

    ms_ked = []
    nms_ked = []
    ms_keda = []
    nms_keda = []
    ms_krvk = []
    nms_krvk = []
    ms_krvka = []
    nms_krvka = []
    ms_tpk = []
    nms_tpk = []
    ms_tpka = []
    nms_tpka = []

    fe_ked = []
    ma_ked = []
    fe_keda = []
    ma_keda = []
    fe_krvk = []
    ma_krvk = []
    fe_krvka = []
    ma_krvka = []
    fe_tpk = []
    ma_tpk = []
    fe_tpka = []
    ma_tpka = []

    und18_ked = []
    f18t30_ked = []
    und18_keda = []
    f18t30_keda = []
    und18_krvk = []
    f18t30_krvk = []
    und18_krvka = []
    f18t30_krvka = []
    und18_tpk = []
    f18t30_tpk = []
    und18_tpka = []
    f18t30_tpka = []
    f31t50_ked = []
    mo50_ked = []
    f31t50_keda = []
    mo50_keda = []
    f31t50_krvk = []
    mo50_krvk = []
    f31t50_krvka = []
    mo50_krvka = []
    f31t50_tpk = []
    mo50_tpk = []
    f31t50_tpka = []
    mo50_tpka = []

    hig_ked = []
    lo_ked = []
    hig_keda = []
    lo_keda = []
    hig_krvk = []
    lo_krvk = []
    hig_krvka = []
    lo_krvka = []
    hig_tpk = []
    lo_tpk = []
    hig_tpka = []
    lo_tpka = []
    with open('results.csv', 'r', encoding="utf-8") as f_obj:
        for row in f_obj:
            row = row.split('\t')
            if row[2] == 'русский' and row[6] == 'кед':
                rus_ked.append(row[6])
            if row[2] == 'русский' and row[6] == 'кеда':
                rus_keda.append(row[6])
            if row[2] == 'не русский' and row[6] == 'кед':
                nrus_ked.append(row[6])
            if row[2] == 'не русский' and row[6] == 'кеда':
                nrus_keda.append(row[6])
            if row[2] == 'русский' and row[7] == 'кроссовок':
                rus_krvk.append(row[7])
            if row[2] == 'русский' and row[7] == 'кроссовка':
                rus_krvka.append(row[7])
            if row[2] == 'не русский' and row[7] == 'кроссовок':
                nrus_krvk.append(row[7])
            if row[2] == 'не русский' and row[7] == 'кроссовка':
                nrus_krvka.append(row[7])
            if row[2] == 'русский' and row[8] == 'тапок\n':
                rus_tpk.append(row[8])
            if row[2] == 'русский' and row[8] == 'тапка\n':
                rus_tpka.append(row[8])
            if row[2] == 'не русский' and row[8] == 'тапок\n':
                nrus_tpk.append(row[8])
            if row[2] == 'не русский' and row[8] == 'тапка\n':
                nrus_tpka.append(row[8])

            if row[3] == 'Москва и МО' and row[6] == 'кед':
                ms_ked.append(row[6])
            if row[3] == 'Москва и МО' and row[6] == 'кеда':
                ms_keda.append(row[6])
            if row[3] == 'Не Москва и МО' and row[6] == 'кед':
                nms_ked.append(row[6])
            if row[3] == 'Не Москва и МО' and row[6] == 'кеда':
                nms_keda.append(row[6])
            if row[3] == 'Москва и МО' and row[7] == 'кроссовок':
                ms_krvk.append(row[7])
            if row[3] == 'Москва и МО' and row[7] == 'кроссовка':
                ms_krvka.append(row[7])
            if row[3] == 'Не Москва и МО' and row[7] == 'кроссовок':
                nms_krvk.append(row[7])
            if row[3] == 'Не Москва и МО' and row[7] == 'кроссовка':
                ms_krvka.append(row[7])
            if row[3] == 'Москва и МО' and row[8] == 'тапок\n':
                ms_tpk.append(row[8])
            if row[3] == 'Москва и МО' and row[8] == 'тапка\n':
                ms_tpka.append(row[8])
            if row[3] == 'Не Москва и МО' and row[8] == 'тапок\n':
                nms_tpk.append(row[8])
            if row[3] == 'Не Москва и МО' and row[8] == 'тапка\n':
                nms_tpka.append(row[8])

            if row[4] == 'женский' and row[6] == 'кед':
                fe_ked.append(row[6])
            if row[4] == 'женский' and row[6] == 'кеда':
                fe_keda.append(row[6])
            if row[4] == 'мужской' and row[6] == 'кед':
                ma_ked.append(row[6])
            if row[4] == 'мужской' and row[6] == 'кеда':
                ma_keda.append(row[6])
            if row[4] == 'женский' and row[7] == 'кроссовок':
                fe_krvk.append(row[7])
            if row[4] == 'женский' and row[7] == 'кроссовка':
                fe_krvka.append(row[7])
            if row[4] == 'мужской' and row[7] == 'кроссовок':
                ma_krvk.append(row[7])
            if row[4] == 'мужской' and row[7] == 'кроссовка':
                ma_krvka.append(row[7])
            if row[4] == 'женский' and row[8] == 'тапок\n':
                fe_tpk.append(row[8])
            if row[4] == 'женский' and row[8] == 'тапка\n':
                fe_tpka.append(row[8])
            if row[4] == 'мужской' and row[8] == 'тапок\n':
                ma_tpk.append(row[8])
            if row[4] == 'мужской' and row[8] == 'тапка\n':
                ma_tpka.append(row[8])

            if row[1] == 'меньше 18' and row[6] == 'кед':
                und18_ked.append(row[6])
            if row[1] == 'меньше 18' and row[6] == 'кеда':
                und18_keda.append(row[6])
            if row[1] == 'от 19 до 30' and row[6] == 'кед':
                f18t30_ked.append(row[6])
            if row[1] == 'от 19 до 30' and row[6] == 'кеда':
                f18t30_keda.append(row[6])
            if row[1] == 'меньше 18' and row[7] == 'кроссовок':
                und18_krvk.append(row[7])
            if row[1] == 'меньше 18' and row[7] == 'кроссовка':
                und18_krvka.append(row[7])
            if row[1] == 'от 19 до 30' and row[7] == 'кроссовок':
                f18t30_krvk.append(row[7])
            if row[1] == 'от 19 до 30' and row[7] == 'кроссовка':
                f18t30_krvka.append(row[7])
            if row[1] == 'меньше 18' and row[8] == 'тапок\n':
                und18_tpk.append(row[8])
            if row[1] == 'меньше 18' and row[8] == 'тапка\n':
                und18_tpka.append(row[8])
            if row[1] == 'от 19 до 30' and row[8] == 'тапок\n':
                f18t30_tpk.append(row[8])
            if row[1] == 'от 19 до 30' and row[8] == 'тапка\n':
                f18t30_tpka.append(row[8])
            if row[1] == 'от 31 до 50' and row[6] == 'кед':
                f31t50_ked.append(row[6])
            if row[1] == 'от 31 до 50' and row[6] == 'кеда':
                f31t50_keda.append(row[6])
            if row[1] == 'больше 51' and row[6] == 'кед':
                mo50_ked.append(row[6])
            if row[1] == 'больше 51' and row[6] == 'кеда':
                mo50_keda.append(row[6])
            if row[1] == 'от 31 до 50' and row[7] == 'кроссовок':
                f31t50_krvk.append(row[7])
            if row[1] == 'от 31 до 50' and row[7] == 'кроссовка':
                f31t50_krvka.append(row[7])
            if row[1] == 'больше 51' and row[7] == 'кроссовок':
                mo50_krvk.append(row[7])
            if row[1] == 'больше 51' and row[7] == 'кроссовка':
                mo50_krvka.append(row[7])
            if row[1] == 'от 31 до 50' and row[8] == 'тапок\n':
                f31t50_tpk.append(row[8])
            if row[1] == 'от 31 до 50' and row[8] == 'тапка\n':
                f31t50_tpka.append(row[8])
            if row[1] == 'больше 51' and row[8] == 'тапок\n':
                mo50_tpk.append(row[8])
            if row[1] == 'больше 51' and row[8] == 'тапка\n':
                mo50_tpka.append(row[8])

            if row[5] == 'высшее' and row[6] == 'кед':
                hig_ked.append(row[6])
            if row[5] == 'высшее' and row[6] == 'кеда':
                hig_keda.append(row[6])
            if row[5] == 'не высшее' and row[6] == 'кед':
                lo_ked.append(row[6])
            if row[5] == 'не высшее' and row[6] == 'кеда':
                lo_keda.append(row[6])
            if row[5] == 'высшее' and row[7] == 'кроссовок':
                hig_krvk.append(row[7])
            if row[5] == 'высшее' and row[7] == 'кроссовка':
                hig_krvka.append(row[7])
            if row[5] == 'не высшее' and row[7] == 'кроссовок':
                lo_krvk.append(row[7])
            if row[5] == 'не высшее' and row[7] == 'кроссовка':
                lo_krvka.append(row[7])
            if row[5] == 'высшее' and row[8] == 'тапок\n':
                hig_tpk.append(row[8])
            if row[5] == 'высшее' and row[8] == 'тапка\n':
                hig_tpka.append(row[8])
            if row[5] == 'не высшее' and row[8] == 'тапок\n':
                lo_tpk.append(row[8])
            if row[5] == 'не высшее' and row[8] == 'тапка\n':
                lo_tpka.append(row[8])
    rus_km = len(rus_ked)
    rus_kf = len(rus_keda)
    nrus_km = len(nrus_ked)
    nrus_kf = len(nrus_keda)
    rus_krm = len(rus_krvk)
    rus_krf = len(rus_krvka)
    nrus_krm = len(nrus_krvk)
    nrus_krf = len(nrus_krvka)
    rus_tm = len(rus_tpk)
    rus_tf = len(rus_tpka)
    nrus_tm = len(nrus_tpk)
    nrus_tf = len(nrus_tpka)

    m_km = len(ms_ked)
    m_kf = len(ms_keda)
    nm_km = len(nms_ked)
    nm_kf = len(nms_keda)
    m_krm = len(ms_krvk)
    m_krf = len(ms_krvka)
    nm_krm = len(nms_krvk)
    nm_krf = len(nms_krvka)
    m_tm = len(ms_tpk)
    m_tf = len(ms_tpka)
    nm_tm = len(nms_tpk)
    nm_tf = len(nms_tpka)

    male_km = len(ma_ked)
    male_kf = len(ma_keda)
    fe_km = len(fe_ked)
    fe_kf = len(fe_keda)
    male_krm = len(ma_krvk)
    male_krf = len(ma_krvka)
    fe_krm = len(fe_krvk)
    fe_krf = len(fe_krvka)
    male_tm = len(ma_tpk)
    male_tf = len(ma_tpka)
    fe_tm = len(fe_tpk)
    fe_tf = len(fe_tpka)

    l18_km = len(und18_ked)
    le18_kf = len(und18_keda)
    from18_km = len(f18t30_ked)
    from18_kf = len(f18t30_keda)
    le18_krm = len(und18_krvk)
    le18_krf = len(und18_krvka)
    from18_krm = len(f18t30_krvk)
    from18_krf = len(f18t30_krvka)
    le18_tm = len(und18_tpk)
    le18_tf = len(und18_tpka)
    from18_tm = len(f18t30_tpk)
    from18_tf = len(f18t30_tpka)
    from30_km = len(f31t50_ked)
    from30_kf = len(f31t50_keda)
    fr50_km = len(mo50_ked)
    fr50_kf = len(mo50_keda)
    from30_krm = len(f31t50_krvk)
    from30_krf = len(f31t50_krvka)
    fr50_krm = len(mo50_krvk)
    fr50_krf = len(mo50_krvka)
    from30_tm = len(f31t50_tpk)
    from30_tf = len(f31t50_tpka)
    fr50_tm = len(mo50_tpk)
    fr50_tf = len(mo50_tpka)

    high_km = len(hig_ked)
    high_kf = len(hig_keda)
    low_km = len(lo_ked)
    low_kf = len(lo_keda)
    high_krm = len(hig_krvk)
    high_krf = len(hig_krvka)
    low_krm = len(lo_krvk)
    low_krf = len(lo_krvka)
    high_tm = len(hig_tpk)
    high_tf = len(hig_tpka)
    low_tm = len(lo_tpk)
    low_tf = len(lo_tpka)
    return render_template('statistic.html', rus_km=rus_km, rus_kf=rus_kf,
                           nrus_km=nrus_km, nrus_kf=nrus_kf, rus_krm=rus_krm, rus_krf=rus_krf,
                           nrus_krm=nrus_krm, nrus_krf=nrus_krf, rus_tm=rus_tm, rus_tf=rus_tf,
                           nrus_tm=nrus_tm, nrus_tf=nrus_tf,
                           m_km=m_km, m_kf=m_kf, nm_km=nm_km, nm_kf=nm_kf, m_krm=m_krm, m_krf=m_krf,
                           nm_krm=nm_krm, nm_krf=nm_krf, m_tm=m_tm, m_tf=m_tf, nm_tm=nm_tm, nm_tf=nm_tf,
                           male_km=male_km, male_kf=male_kf, fe_km=fe_km, fe_kf=fe_kf, male_krm=male_krm,
                           male_krf=male_krf, fe_krm=fe_krm, fe_krf=fe_krf, male_tm=male_tm, male_tf=male_tf,
                           fe_tm=fe_tm, fe_tf=fe_tf,
                           l18_km=l18_km, le18_kf=le18_kf, from18_km=from18_km, from18_kf=from18_kf,
                           le18_krm=le18_krm, le18_krf=le18_krf, from18_krm=from18_krm, from18_krf=from18_krf,
                           le18_tm=le18_tm, le18_tf=le18_tf, from18_tm=from18_tm,
                           from18_tf=from18_tf, from30_km=from30_km, from30_kf=from30_kf,
                           fr50_km=fr50_km, fr50_kf=fr50_kf, from30_krm=from30_krm,
                           from30_krf=from30_krf, fr50_krm=fr50_krm, fr50_krf=fr50_krf,
                           from30_tm=from30_tm, from30_tf=from30_tf, fr50_tm=fr50_tm, fr50_tf=fr50_tf,
                           high_km=high_km, high_kf=high_kf, low_km=low_km, low_kf=low_kf,
                           high_krm=high_krm, high_krf=high_krf, low_krm=low_krm, low_krf=low_krf,
                           high_tm=high_tm, high_tf=high_tf, low_tm=low_tm, low_tf=low_tf, urls=urls)

if __name__ == '__main__':
    print(dictinf)
    app.run(debug=True)

#
