from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def citata ():
    citata = requests.get("https://api.quotable.io/random").json()# requests.get это запрос к сайту
    if request.method == 'POST':# request.method ' это если нажать на кнопку "Получить цитату"
        citata = requests.get("https://api.quotable.io/random").json() #json это превращение в json
    return render_template('DZ.html', citata=citata) # render_template это отрисовка шаблона

if __name__ == '__main__':
    app.run(debug=True)