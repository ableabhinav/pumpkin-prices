import csv
import os
from pumpkinPrices.models import Pumpkin

path = "/home/abh/drfapi/assignment/a-year-of-pumpkin-prices/"
os.chdir(path)

def run():
	# with open('/home/abh/drfapi/assignment/a-year-of-pumpkin-prices/detroit.csv') as csvfile:
	# 	reader = csv.DictReader(csvfile)
	# 	for row in reader:
	# 		p = Pumpkin(city=row['City Name'], variety=row['Variety'], date=row['Date'], low_price=row['Low Price'], high_price=row['High Price'])
	# 		p.save()
			
	# with open('/home/abh/drfapi/assignment/a-year-of-pumpkin-prices/los-angeles.csv') as csvfile:
	# 	reader = csv.DictReader(csvfile)
	# 	for row in reader:
	# 		p = Pumpkin(city=row['City Name'], variety=row['Variety'], date=row['Date'], low_price=row['Low Price'], high_price=row['High Price'])
	# 		p.save()

	# with open('/home/abh/drfapi/assignment/a-year-of-pumpkin-prices/miami.csv') as csvfile:
	# 	reader = csv.DictReader(csvfile)
	# 	for row in reader:
	# 		p = Pumpkin(city=row['City Name'], variety=row['Variety'], date=row['Date'], low_price=row['Low Price'], high_price=row['High Price'])
	# 		p.save()

	# with open('/home/abh/drfapi/assignment/a-year-of-pumpkin-prices/new-york.csv') as csvfile:
	# 	reader = csv.DictReader(csvfile)
	# 	for row in reader:
	# 		p = Pumpkin(city=row['City Name'], variety=row['Variety'], date=row['Date'], low_price=row['Low Price'], high_price=row['High Price'])
	# 		p.save()

	with open('/home/abh/drfapi/assignment/a-year-of-pumpkin-prices/philadelphia.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			p = Pumpkin(city=row['City Name'], variety=row['Variety'], date=row['Date'], low_price=row['Low Price'], high_price=row['High Price'])
			p.save()

	with open('/home/abh/drfapi/assignment/a-year-of-pumpkin-prices/san-fransisco.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			p = Pumpkin(city=row['City Name'], variety=row['Variety'], date=row['Date'], low_price=row['Low Price'], high_price=row['High Price'])
			p.save()

	with open('/home/abh/drfapi/assignment/a-year-of-pumpkin-prices/st-louis.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			p = Pumpkin(city=row['City Name'], variety=row['Variety'], date=row['Date'], low_price=row['Low Price'], high_price=row['High Price'])
			p.save()