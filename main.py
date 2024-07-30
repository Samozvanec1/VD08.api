from flask import Flask, render_template, request
import requests

app = Flask(__name__)

token = "cad0d21de03e6ec45ce212c3de891f4b"

news_token = "cb8d53e68def4024bfb9b8b8f7a42071"


@app.route('/', methods=['GET', 'POST'])
def index():
    city = "Moscow"
    news = news_api_get()
    weather = get_weather(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
    if request.method == 'POST':
        city = request.form['city']
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"
        weather = get_weather(link)
        news = news_api_get()
    return render_template('index.html', weather=weather, city=city , news=news)
def get_weather(link):
    weather = requests.get(link).json()
    return weather
def news_api_get():
    news = requests.get(f"https://newsapi.org/v2/top-headlines?country=ru&apiKey={news_token}").json()
    return news.get('articles', [])

if __name__ == '__main__':
    app.run(debug=True)