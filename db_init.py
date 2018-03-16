customers = [
	
	{"name": "tennesse"},
	{"name": "caterpillar"},
	{"name": "gilead"},
	{"name": "siemens"},
	{"name": "epsilon"},
	{"name": "anthem"},
	{"name": "redbox"},
	{"name": "united health group"}

]
partners = [
	
	{"name": "teradata"},
	{"name": "ibm"},
	{"name": "kinetica"},
	{"name": "oracle"},
	{"name": "nvidia"},
	{"name": "AWS"}
	
]

markets = [

	{"name": "health care"},
	{"name": "finance and banking industries"},
	{"name": "retail and commerce"},
	{"name": "manufacturing industries"},
	{"name": "telecommunications industries"}

]


products = [
	{"name": "DB Lytix", "description": "DB Lytix™ is Fuzzy Logix’s flagship in-database analytics product, achieving high-performance analytics, up to 100x faster than conventional methods. "},
	{"name": "Fin Lytix", "description": "Fin Lytix, our advanced analytics solution for financial industries was specially developed for the specific complex and challenging industry needs. "},
	{"name": "Saral", "description": "Saral™ is a product which expands the horizons of Fuzzy Logix’s flagship product, DB Lytix™, by providing an interactive Graphical User Interface (GUI), as a plugin on Alteryx, without compromising on key strengths such as performance and scalability."},
	{"name": "AdapteR", "description": "AdapteR is an advanced analytics package that enables R users to perform in-database analytics using Fuzzy Logix' flagship DBLytix™ suite of functions."},
	{"name": "Analytics Consultancy", "description": " With an average of 15+ years of experience our analytics consultants will work with you to establish analytically savvy and agile business strategies that help you achieve your business objectives: whether that is to determine the optimal pricing structure of a new or existing product, predict the success of a marketing campaign or define the KPIs and the drivers that affect the performance of your business."}
]

from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)

db = client['chatbot']

customer_table = db['customers']
for customer in customers:
	customer_table.insert(customer)

partners_table = db['partners']
for partner in partners:
	partners_table.insert(partner)

markets_table = db['markets']
for market in markets:
	markets_table.insert(market)

products_table = db['products']
for product in products:
	products_table.insert(product)


# cinema_table = db['cinemas']
# for cinema in cinema_names:
# 	customer_table.insert(cinema)

# schedule_table = db['schedule']
# for schedule in schedules:
# 	schedule_table.insert(schedule)
