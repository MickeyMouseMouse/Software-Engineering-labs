import requests
from bs4 import BeautifulSoup as bs

def getSoup():
	try:
		request = requests.get("https://www.banki.ru/products/currency/cb/")
		if request.status_code == 200: # OK
			return bs(request.text, "html.parser")
		else:
			return None
	except Exception:
		return None

def getPrice(currency):
	soup = getSoup()
	if soup == None: return None
	tags = soup.find("tr", {"data-currency-code":currency}).find_all("td")
	amount = int(tags[1].text)
	currency_exchange_rate = float(tags[3].text)
	return currency_exchange_rate / amount

def get_amount(string):
	ok = True
	for char in string:
		if not (char.isdigit() or char == '.'):
			ok = False
			break
	if ok:
		return float(string)
	else:
		return None

def main():
	amount = get_amount(input("Amount in rubles: "))
	if amount == None:
		print("Error: Wrong amount.")
		return
	currency = input("Сonvert to: ").upper()
	price = getPrice(currency)
	print("Result:", amount / price, currency, end = "\n\n")

if __name__ == '__main__':
    main()