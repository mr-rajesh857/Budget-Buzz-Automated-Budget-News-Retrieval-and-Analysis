from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    url = "https://www.businesstoday.in/union-budget"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    outer_data = soup.find_all("h3", class_="lst_li_rhs")
    
    news = []
    for data in outer_data:
        news.append(data.a['title'])
    
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)
