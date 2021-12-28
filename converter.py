import requests
from bs4 import BeautifulSoup as bs

def getSoup():
	request = requests.get("https://www.banki.ru/products/currency/cb/")
	if request.status_code == 200: # OK
		return bs(request.text, "html.parser")

def getPrice(currency):
	soup = getSoup()
	tags = soup.find("tr", {"data-currency-code":currency}).find_all("td")
	amount = int(tags[1].text)
	currency_exchange_rate = float(tags[3].text)
	return currency_exchange_rate / amount

def main():
	amount = float(input("Amount in rubles: "))
	currency = input("Сonvert to: ").upper()
	price = getPrice(currency)
	print("Result:", amount / price, currency, end = "\n\n")

if __name__ == '__main__':
    main()
