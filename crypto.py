import requests
from termcolor import colored
from terminaltables import AsciiTable

response = requests.get('https://api.coinmarketcap.com/v1/ticker/')
json_data = response.json()
coins = [item for item in json_data]

table_data = []
table = AsciiTable(table_data)

def crypto(i=None):
	c = len(coins)
	c += 1
	num = 1

	if i is None:
		for index, x in enumerate(coins):		
			price = str(x['price_usd'])
			percent_change_24h = str(x['percent_change_24h'])
			if percent_change_24h[0] == '-':
				percent_change_24h = colored(percent_change_24h, 'red') + '%'
			else:
				percent_change_24h = colored(percent_change_24h, 'green') + '%'
			name = str(x['name'])
			rank = str(x['rank'])

			table_data.append([])
			table_data[index].append(rank)
			table_data[index].append(name)
			table_data[index].append(price)				
			table_data[index].append(percent_change_24h)

	else:
		for index, x in enumerate(coins):
			if i == x['id']:
				price = str(x['price_usd'])
				percent_change_24h = str(x['percent_change_24h'])
				if percent_change_24h[0] == '-':
					percent_change_24h = colored(percent_change_24h, 'red') + '%'
				else:
					percent_change_24h = colored(percent_change_24h, 'green') + '%'
				name = str(x['name'])
				rank = str(x['rank'])

				table_data.append([])
				table_data[index].append(rank)
				table_data[index].append(name)
				table_data[index].append(price)				
				table_data[index].append(percent_change_24h)

	table_data.insert(0, ['Rank', 'Name', 'Price', '24h % Change'])
	print(table.table)
		

crypto()