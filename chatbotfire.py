# import the flask 
from flask import Flask, render_template, request, jsonify
from firebase import firebase


app = Flask(__name__)
firebase = firebase.FirebaseApplication("https://tester-2deea.firebaseio.com", None)
print("firebase variable on the start is ", firebase)


# import chatterbot and the trainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# connection from mongo db
# from pymongo import MongoClient
# client = MongoClient()
# client = MongoClient('localhost', 27017)

# db = client['chatbot']

# customer_table = db['customers']
# print("abs is equal to ", customer_table)

# getting the data from mongodb to local machine
customer_table = firebase.get('/customers', None)
# print("bldhgjnsfgjndkf jksfgnjsfgnjnfgkndfgn dfjgndjfgn",customer_table)
partner_table = firebase.get('/partners', None)
market_table = firebase.get('/markets', None)
product_table = firebase.get('/products', None)
arrCustomers = customer_table[1:]
arrPartners = partner_table[1:]
arrMarkets = market_table[1:]
arrProducts = product_table[1:]

# for customer in customer_table.find():
#     arrCustomers.append(customer)
print("customers is ", arrCustomers)
print("partners is ", arrPartners)
print("markets is ", arrMarkets)
print("products is ", arrProducts)





# define your dataset of questions and the respective methods here and it will train on 
info_customer_dataset = ["who are your customers", "We are in service of tennesse, caterpillar, gilead, siemens, epsilon, anthem, redbox, united health group.",
"is oracle your client?", "info_customer", 
"have you worked with oracle", "info_customer",
"is teradata your client", "info_customer",
"have you worked for hdfc", "info_customer",
"what is your relationship with teradata", "info_customer",
"is bank of america your customer", "info_customer"]

info_partner_dataset = ["who are your partners", "We are in partnership with teradata, ibm, kinetica, oracle, nvidia, AWS and many more",
"tell me about your partners ?","We are in partnership with teradata, ibm, kinetica, oracle, nvidia, AWS and many more",    "is teradata your partner?", "info_partner",
"are you partnered with ibm ? ", "info_partner",
"have your partnered with AWS? ", "info_partner",
"are you in partnership with kinetica?", "info_partner"]

dataset = ["In what industries can your product be used", "Our advanced, in-database analytics solutions are used by the healthcare and pharma industriesfinance and banking industries,  retail and commerce, manufacturing industries, telecommunications industries",
"what are the industries in which you are working ?", "Our advanced, in-database analytics solutions are used by the healthcare and pharma industriesfinance and banking industries,  retail and commerce, manufacturing industries, telecommunications industries",
"what is your market", "Our advanced, in-database analytics solutions are used by the healthcare and pharma industriesfinance and banking industries,  retail and commerce, manufacturing industries, telecommunications industries",
"what is your target market?", "Our advanced, in-database analytics solutions are used by the healthcare and pharma industriesfinance and banking industries,  retail and commerce, manufacturing industries, telecommunications industries",
"what is fuzzylogix? ", "In 2007 two ex-Bank Of America colleagues  - Partha Sen and Mike Upchurch – formed Fuzzy Logix. With a combined passion for solving problems with quantitative methods, data mining and pattern recognition, and a foresight of how businesses would increasingly collect information and need to achieve actionable insight from this data, they created a business that transformed data analytics. By performing the analytics directly where the data resides and eliminating the need to move it, in-database analytics was created.",
"what does your company do?", "In 2007 two ex-Bank Of America colleagues  - Partha Sen and Mike Upchurch – formed Fuzzy Logix. With a combined passion for solving problems with quantitative methods, data mining and pattern recognition, and a foresight of how businesses would increasingly collect information and need to achieve actionable insight from this data, they created a business that transformed data analytics. By performing the analytics directly where the data resides and eliminating the need to move it, in-database analytics was created."
"tell me where you belong to", "Fuzzylogix",
"tell me who do you work for?", "fuzzylogix",
"who is the ceo of the company", "Partha Sen",
"tell me about your company", "In 2007 two ex-Bank Of America colleagues  - Partha Sen and Mike Upchurch – formed Fuzzy Logix. With a combined passion for solving problems with quantitative methods, data mining and pattern recognition, and a foresight of how businesses would increasingly collect information and need to achieve actionable insight from this data, they created a business that transformed data analytics. By performing the analytics directly where the data resides and eliminating the need to move it, in-database analytics was created. Now a global business with more than 50 employees, Fuzzy Logix is proud of its roster of clients for whom we have helped achieve unprecedented time, cost and resource savings with their data analytics. We are partners with some of the best analytics platforms in the industry, and we continue to develop our products and services to meet the ever-increasing big data challenges faced by businesses and organisations.",
"tell me about fuzzylogix", "In 2007 two ex-Bank Of America colleagues  - Partha Sen and Mike Upchurch – formed Fuzzy Logix. With a combined passion for solving problems with quantitative methods, data mining and pattern recognition, and a foresight of how businesses would increasingly collect information and need to achieve actionable insight from this data, they created a business that transformed data analytics. By performing the analytics directly where the data resides and eliminating the need to move it, in-database analytics was created. Now a global business with more than 50 employees, Fuzzy Logix is proud of its roster of clients for whom we have helped achieve unprecedented time, cost and resource savings with their data analytics. We are partners with some of the best analytics platforms in the industry, and we continue to develop our products and services to meet the ever-increasing big data challenges faced by businesses and organisations.",
"What is the history of the company", "In 2007 two ex-Bank Of America colleagues  - Partha Sen and Mike Upchurch – formed Fuzzy Logix. With a combined passion for solving problems with quantitative methods, data mining and pattern recognition, and a foresight of how businesses would increasingly collect information and need to achieve actionable insight from this data, they created a business that transformed data analytics. By performing the analytics directly where the data resides and eliminating the need to move it, in-database analytics was created. Now a global business with more than 50 employees, Fuzzy Logix is proud of its roster of clients for whom we have helped achieve unprecedented time, cost and resource savings with their data analytics. We are partners with some of the best analytics platforms in the industry, and we continue to develop our products and services to meet the ever-increasing big data challenges faced by businesses and organisations.",
"who is Varsha Lalwani? ", "Our Mentor",
"will we win", "we don't play for winning but we win when we play types"
]

dataset1 = [

"tell me who you are ", "Hi! I am Fuzzy Logix Bot made with Love by bugAASURS",
"tell me about yourself", "Hi! I am Fuzzy Logix Bot made with Love by bugAASURS",
"who are you", "Hi! I am Fuzzy Logix Bot made with Love by bugAASURS",
"who made you", "Hi! I am Fuzzy Logix Bot made with Love by bugAASURS",
"are you better than siri", "of course",
"tell me a joke", "LOL I am a BigData Analytics company owned chatbot. Let's focus on work."

]


info_market_dataset = ["can your product be applied in health care", "info_market", "are you working in finance and banking ", "info_market",
"can your work be applied in retail and commerce", "info_market",
"are you working in manufacturing", "info_market"]

info_product_dataset = ["tell about your products", "info_product",
"what are your products", "info_product",
"what is DBLytix", "info_product",
"tell me about some of your products", "info_product"
"what does dblytix do ", "info_product",
"what is finlytix", "info_product",
"tell about adapter", "info_product",
"tell me about saral", "info_product",
"tell me something about DB Lytix", "info_product"]

chatterbot = ChatBot("FLchatbot")


chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

chatterbot.set_trainer(ListTrainer)

chatterbot.train([
    "Hi",
    "What would you like to find ? I can give information about the company",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
    "how are you ?",
    "I am fine. What would you like to find?",
    "bye... for more information contact at www.fuzzylogix.com/about-fuzzy-logix/contact-us/",
    "have a good time. For more information contact at http://www.fuzzylogix.com/about-fuzzy-logix/contact-us/",
    "DB Lytix",
    "update_context_and_repeat_last_action",
    "Fin Lytix",
    "update_context_and_repeat_last_action",
    "AdapteR",
    "update_context_and_repeat_last_action",
    "Saral",
    "update_context_and_repeat_last_action",
    "Analytics Consultancy",
    "update_context_and_repeat_last_action"
])

chatterbot.train(info_customer_dataset)
chatterbot.train(info_partner_dataset)
chatterbot.train(dataset)
chatterbot.train(info_market_dataset)
chatterbot.train(info_product_dataset)
chatterbot.train(dataset1)



context = {}




@app.route("/")
def hello():
    return render_template('chat.html')


@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])
    print(message)
    bot_response = chatterbot.get_response(message)
    print("bot {0}".format(bot_response))
    update_context(message, bot_response)
    final_response = create_response(bot_response)
    if(final_response):
        print("final {0}".format(final_response))
        return jsonify({'status':'OK','answer':final_response})
    return jsonify({'status':'OK','answer':str(bot_response)})

def update_context(message, bot_response):
    print("inside update_context")

    customers = context.get("customers")
    print("context1 is ", context)
    print("customer in update_context is ", customers)
    if(customers is None):
        # print("message in update context is  ", message)
        customers = find_customers(message)
        context['customers'] = customers
        print("context in if else in update context1 ", context)

    partners = context.get("partners")
    print("context2 is ", context)
    print("partner in update_context is ", partners)
    if(partners is None):
        # print("message in update context is  ", message)
        partners = find_partners(message)
        context['partners'] = partners
        print("context in if else in update context2 ", context)


    markets = context.get("markets")
    print("context3 is ", context)
    print("market in update_context is ", markets)
    if(markets is None):
        # print("message in update context is  ", message)
        markets = find_markets(message)
        context['markets'] = markets
        print("context in if else in update context3 ", context)

    products = context.get("products")
    print("context4 is ", context)
    print("products in update_context is ", products)
    if(products is None):
        # print("message in update context is  ", message)
        products = find_products(message)
        context['products'] = products
        print("context in if else in update context3 ", context)

    return 

def info_customer():
    response = ""
    customers = context.get('customers')
    print("customer context in info customer is", customers)
    if(customers is None):
        context['customers'] = None;
        response = "not yet... but we are constantly increasing our client base"
    else:
        for i in range(0, len(customers) - 1 ):
            response = customers[i] + ", "
        response = response + customers[len(customers)-1] 
        if(len(customers) > 1):
            response = response +  " are our brilliant customers."
        else:
            response = response + " is our brilliant customer."
        # response = response + "our brilliant customer."
    return response

def info_partner():
    response = ""
    partners = context.get('partners')
    print("partner context in info partner is", partners)
    if(partners is None):
        context['partners'] = None;
        response = "Maybe we shall partner with them in future."
    else:
        for i in range(0, len(partners) - 1 ):
            response = partners[i] + ", "
        response = response + partners[len(partners)-1] 
        if(len(partners) > 1):
            response = response +  " are our brilliant partners."
        else:
            response = response + " is our brilliant partner."
    return response

def info_market():
    response = ""
    markets = context.get('markets')
    print("market context in info market is", markets)
    if(markets is None):
        context['markets'] = None;
        response = "We are expanding our horizons to all markets"
    else:
        response = "We are working in "
        for i in range(0, len(markets) - 1 ):
            response = markets[i] + ", "
        response = response + markets[len(markets)-1] 
        # if(len(markets) > 1):
        #     response = response 
        # else:
        #     response = response + " is a brilliant market."
    return response

def info_product():
    response = ""
    products = context.get("products")
    # print("products is --------------" , products)
    # print("product context in info product is", products)
    if(products is None):
        context["last_response"] = "info_product"
        return "Currently, we provide the following products: DB Lytix, Fin Lytix, Saral, AdapteR and we also provide Analytics Consultancy. Which product would you like to know about in detail?"
    else:
        context["last_response"] = None
        return products[0]["description"]

def update_context_and_repeat_last_action():
    if(context.get("last_response") == "info_product"):
        return info_product()
    return "sorry, please try to contact us at aman.jain@fuzzylogix.com"

def create_response(bot_response):
    if(bot_response=="info_customer"):
        return info_customer()
    elif(bot_response=="info_partner"):
        return info_partner()
    elif(bot_response=="info_market"):
        return info_market()
    elif(bot_response=="info_product"):
        return info_product()
    elif(bot_response=="update_context_and_repeat_last_action"):
        return update_context_and_repeat_last_action()
    else: 
        context["customers"] = None
        context["partners"] = None
        context["markets"] = None
        context["products"] = None


def find_customers(message):
    customers = []
    print("arrCustomers -> {0}".format(arrCustomers))
    for customer in arrCustomers:
        if(message.find(customer["name"])>-1):
            customers.append(customer["name"])
    if(len(customers)==0):
        return None
    return customers

def find_partners(message):
    partners = []
    print("arrPartners -> {0}".format(arrPartners))
    for partner in arrPartners:
        if(message.find(partner["name"])>-1):
            partners.append(partner["name"])
    if(len(partners)==0):
        return None
    return partners

def find_markets(message):
    markets = []
    print("arrMarkets -> {0}".format(arrMarkets))
    for market in arrMarkets:
        if(message.find(market["name"])>-1):
            markets.append(market["name"])
    if(len(markets)==0):
        return None
    return markets


def find_products(message):
    products = []
    print("arrProducts -> {0}".format(arrProducts))
    for product in arrProducts:
        if(message.find(product["name"])>-1):
            products.append(product)
    if(len(products)==0):
        return None
    return products



if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)
