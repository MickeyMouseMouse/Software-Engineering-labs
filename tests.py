import converter, re


def run_test(input_data):
	output = []
	def _input(item):
		output.append(item)
		return input_data.pop(0)

	converter.input = _input
	converter.print = lambda item: output.append(item)
	converter.main()
	return output


def test_1():
	output = run_test(['73', 'usd'])

	assert output[0] == "Supported currencies: USD EUR AUD CAD BYN KZT UAH GBP CZK CHF JPY"
	assert output[1] == "Amount in rubles: "
	assert output[2] == "Сonvert to: "
	assert re.fullmatch("Result: ([0-9]+.)?[0-9]+ USD", output[3])


def test_2():
	output = run_test(['100.56', 'EUR'])

	assert output[0] == "Supported currencies: USD EUR AUD CAD BYN KZT UAH GBP CZK CHF JPY"
	assert output[1] == "Amount in rubles: "
	assert output[2] == "Сonvert to: "
	assert re.fullmatch("Result: ([0-9]+.)?[0-9]+ EUR", output[3])
	

def test_with_comma():
	output = run_test(['100,56', 'EUR']) # "," instead of "."

	assert output[0] == "Supported currencies: USD EUR AUD CAD BYN KZT UAH GBP CZK CHF JPY"
	assert output[1] == "Amount in rubles: "
	assert output[2] == "Error: Wrong amount."


def test_with_wrong_amount():
	output = run_test(['1ww3', 'usd'])
	
	assert output[0] == "Supported currencies: USD EUR AUD CAD BYN KZT UAH GBP CZK CHF JPY"
	assert output[1] == "Amount in rubles: "
	assert output[2] == "Error: Wrong amount."


def test_with_wrong_currency():
	output = run_test(['123', 'abc'])
	
	assert output[0] == "Supported currencies: USD EUR AUD CAD BYN KZT UAH GBP CZK CHF JPY"
	assert output[1] == "Amount in rubles: "
	assert output[2] == "Сonvert to: "
	assert output[3] == "Error: Unknown currency."