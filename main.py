import requests

cur_name = input("Currency code according to ISO 4217 ")
url = f"https://www.nbrb.by/api/exrates/rates/{cur_name}?parammode=2"
r = requests.get(url)
usd = r.json()

print(f"\n{usd['Cur_OfficialRate']}BYN as of {usd['Date']}")
