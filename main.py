import datetime as dt

""" Не оформлены комментарии к классам и методам, необходимо оформить
    в виде Docstring.
    https://www.python.org/dev/peps/pep-0257/
    
    Для классов и методов необходимо добавить type annotations.
    https://semakin.dev/2020/06/type_hints/
"""
class Record:
    # значение по умолчанию лучше определить через None
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        # именовать переменные в Python принято с маленькой буквы 
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # условие можно записать короче, в виде: 0 <= a < 7
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        # вместо x можно назвать переменную более понятно, например calories_remained 
        x = self.limit - self.get_today_stats()
        if x > 0:
            # \ для переноса не используется
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # else тут можно убрать т.к. иначе мы попадаем сюда. 
        else:
            # скобки можно убрать
            return('Хватит есть!')


class CashCalculator(Calculator):
    # коментарии являются переводом именования констант, можно убрать
    # вместо float короче будет записать число с точкой
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            cash_remained == 1.00
            currency_type = 'руб'
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    def get_week_stats(self):
        super().get_week_stats()

""" Не написаны сценарии использования классов (П.3 задания), необходимо
    дописать закрыв конструкцией if __name__ == "__main__".
    https://pyneng.readthedocs.io/ru/latest/book/11_modules/if_name_main.html
"""

calc = CashCalculator(1000)
print(calc.EURO_RATE)