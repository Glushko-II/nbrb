import requests
import xlrd


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


def get_url():
    pass


currency = get_correct_currency()

url = f"https://www.nbrb.by/api/exrates/rates/{currency}?parammode=2"
r = requests.get(url)
currency_rate = r.json()

print(f"\n{currency_rate['Cur_OfficialRate']}BYN as of {currency_rate['Date']}")
