from flask import Flask, render_template, request
import requests

app = Flask(__name__)

HTTP_PROXY = "126.179.0.206:9090"
HTTPS_PROXY = "126.179.0.206:9090"
FTP_PROXY = "ftp://126.179.0.206:9090"

PROXY_DICT = {
    "http": HTTP_PROXY,
    "https": HTTPS_PROXY,
    "ftp": FTP_PROXY
}


@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' +
                     zipcode+',pl&appid=ae75f9863b9eac983c31433a0edfe79d')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15)  # * 1.8 + 32
    # temp_f += "\n =========================" + str(r.json())
    tt = str(json_object)
    return render_template('temperature.html', temp=temp_f, jj=tt)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
