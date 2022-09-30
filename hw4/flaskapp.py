from flask import Flask
from flask import request
from utils import currency_rate
from db_functions import get_filtered_customers, count_customers_firstname, sum_of_orders
app = Flask(__name__)


@app.route('/')
def home():
    return '<b>Для проверки используйте --> </b> http://127.0.0.1:5000/rates?date=21.09.2022&bank=PB&a1=UAH&b2=USD' \
           '<br>Актуальные ссылки для проверки --> http://127.0.0.1:5000/filtered_customers</br>'\
                                   '<br>http://127.0.0.1:5000/count_first_name</br>'\
                                   '<br>http://127.0.0.1:5000/total_amount</br>'\
'<br>А также хотел сказать спасибо за интересные уроки, получилось отличное и живое начало курса!</br>'\


@app.route('/rates', methods=['GET'])
def rates():
    date = request.args.get('date', default='21.12.2022')
    bank = request.args.get('bank', default='PB')
    curr_a = request.args.get('curr_a', default='UAH')
    curr_b = request.args.get('curr_b', default='USD')
    result = currency_rate(date=date, bank=bank, curr_a=curr_a, curr_b=curr_b)
    return result


@app.route("/filtered_customers", methods=['GET'])
def filtered_customers():
    city = request.args.get('city', default=None)
    state = request.args.get('state', default=None)

    return get_filtered_customers(city=city, state=state)


@app.route("/count_first_name", methods=['GET'])
def count_first_name():
    return count_customers_firstname()


@app.route("/total_amount", methods=['GET'])
def total_amount():
    return sum_of_orders()


if __name__ == '__main__':
    app.run(debug=True)
