import requests
import os

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

current_dir = os.path.dirname(os.path.abspath(__file__))
DE = os.path.join(current_dir, os.path.abspath("DE.txt"))
ES = os.path.join(current_dir, os.path.abspath("ES.txt"))
FR = os.path.join(current_dir, os.path.abspath("FR.txt"))

def translate_it(from_lang, to_lang, text_path, result_path):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    with open(text_path) as f:
        text = f.read()
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{0}-{1}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    result = ''.join(json_['text'])
    with open(result_path, "w") as f:
        f.write(result)

while(True):
    lang = input("Введите язык с которого перевести:\n"
          "DE - немецкий\n"
          "ES - испанский\n"
          "FR - французский\n"
          "e - выход из программы\n"
    )

    if lang == "DE":
        translate_it("de", "ru", DE, os.path.join(current_dir, "result_DE.txt"))
        break
    elif lang == "ES":
        translate_it("es", "ru", ES, os.path.join(current_dir, "result_ES.txt"))
        break
    elif lang == "FR":
        translate_it("fr", "ru", FR, os.path.join(current_dir, "result_FR.txt"))
        break
    elif lang == "e":
        break

# requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))