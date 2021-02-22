import requests


def get_currencies_iso():
    import xlrd
    try:
        book = xlrd.open_workbook("list_of_currencies.xls")
    except FileNotFoundError:
        return None
    else:
        sh = book.sheet_by_index(0)
        return sh.col_values(colx=2, start_rowx=4, end_rowx=280)


def get_currency():
    pass


def get_url(currency: str, url: str = None):
    pass


currency = input("Currency code according to ISO 4217 ")

url = f"https://www.nbrb.by/api/exrates/rates/{currency}?parammode=2"
r = requests.get(url)
usd = r.json()

print(f"\n{usd['Cur_OfficialRate']}BYN as of {usd['Date']}")
