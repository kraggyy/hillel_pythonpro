from flask import Flask
from flask import request
from utils import currency_rate

app = Flask(__name__)
@app.route('/')
def home():
    return '<b>Для проверки используйте --> </b> http://127.0.0.1:5000/rates?date=21.09.2022&bank=PB&a1=UAH&b2=USD'

@app.route('/rates', methods=['GET'])
def rates():
    date = request.args.get('date', default='21.12.2022')
    bank = request.args.get('bank', default='PB')
    curr_a = request.args.get('curr_a', default='UAH')
    curr_b = request.args.get('curr_b', default='USD')
    result = currency_rate(date=date, bank=bank, curr_a=curr_a, curr_b=curr_b)
    return result


if __name__ == '__main__':
    app.run(debug=True)
