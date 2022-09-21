import requests

def currency_rate(date: str, bank: str, curr_a: str, curr_b: str):

    response = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}')
    json = response.json()
    exchangeRate = json.get('exchangeRate')

    if response.status_code == 200:
        if bank == 'PB':
            for i in range(len(exchangeRate)):
                if exchangeRate[i].get('baseCurrency') == curr_a and exchangeRate[i].get('currency') == curr_b:
                    purchaseRate = exchangeRate[i].get('purchaseRate')
                    saleRate = exchangeRate[i].get('saleRate')
                    return f'Курс ПриватБанка на {date}при конвертации {curr_a} в {curr_b} для покупки {purchaseRate} и для продажи {saleRate}'
            raise KeyError(f'Нет курса обмена {curr_a} в {curr_b}')
        elif bank == 'NB':
            for i in range(len(exchangeRate)):
                if exchangeRate[i].get('baseCurrency') == curr_a and exchangeRate[i].get('currency') == curr_b:
                    purchaseRateNB = exchangeRate[i].get('purchaseRateNB')
                    saleRateNB = exchangeRate[i].get('saleRateNB')
                    return f'Курс НБУ на {date} при конвертации  {curr_a} в {curr_b} для покупки  {purchaseRateNB}  и для продажи { saleRateNB}'
            raise KeyError(f'Нет курса обмена {curr_a} в {curr_b}')
        else:
            return f'Банка: {bank} -> не существует!'

    else:
        return f'API Error (status_code: {response.status_code})'

#print(currency_rate('01.12.2018','PB','UAH','USD'))