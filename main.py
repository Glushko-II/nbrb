import requests
import xlrd


class MyError(Exception):
    pass


def get_currencies_iso():
    try:
        book = xlrd.open_workbook("list_of_currencies.xls")
    except FileNotFoundError as ex:
        print(f"File not found: {ex}")
    else:
        sh = book.sheet_by_index(0)
        return sh.col_values(colx=2, start_rowx=4, end_rowx=280)


def get_correct_currency():
    while True:
        currency_name = input("Currency code according to ISO 4217 ")
        currencies_iso = get_currencies_iso()
        if currency_name.upper() in currencies_iso:
            break
        else:
            print("Incorrect currency name entered!")
    return currency_name


def get_url(url: str):
    try:
        if requests.get(url).status_code != 200:
            raise MyError()
    except MyError:
        print(f"Unsuccessful response on request")
    else:
        return requests.get(url).json()


def print_response(currency_rate: dict):
    try:
        print(f"\n{currency_rate['Cur_OfficialRate']}BYN as of {currency_rate['Date']}")
    except TypeError:
        pass



currency = get_correct_currency()
url = f"https://www.nbrb.by/api/exrates/rates/{currency}?parammode=2"
print_response(get_url(url))
