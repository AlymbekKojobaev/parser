from bs4 import BeautifulSoup as bs
import requests
import psycopg2

connection = psycopg2.connect(
    dbname = 'itc',
    user = 'postgres',
    password = 'slashjoker14',
    host = 'localhost'
)
cursor = connection.cursor()

create = '''CREATE TABLE meats (
    user_id SERIAL PRIMARY KEY,
    image_link VARCHAR(300) NOT NULL,
    product_name VARCHAR(300) NOT NULL,
    price VARCHAR(300) NOT NULL
);'''
cursor.execute(create)
cursor.connection.commit()


HOST = 'https://globus-online.kg/catalog/myaso_ptitsa_ryba/'
HEADERS ={
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

globus_page = requests.get(HOST,headers=HEADERS).text

data = bs(globus_page,'html.parser')

view_showcase = data.find('div', attrs={"id":"view-showcase"})

all_cards = view_showcase.find_all('div', class_ = 'list-showcase__part-main')

for card in all_cards:
    image_link = card.find('div', class_='list-showcase__picture').a.img.get('src')
    product_name = card.find('div', class_='list-showcase__name-rating').a.text
    price = card.find('div', class_='list-showcase__prices').find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text

    a = f'''INSERT INTO meats (image_link, product_name, price)
        VALUES (\'{image_link}\', \'{product_name}\', \'{price}\');'''

    cursor.execute(a)
    connection.commit()


















# from bs4 import BeautifulSoup as bs
# import requests
# import psycopg2
#
# connection = psycopg2.connect(
#     dbname = 'itc',
#     user = 'postgres',
#     password = 'slashjoker14',
#     host = 'localhost'
# )
# cursor = connection.cursor()
#
#
#
# create = '''CREATE TABLE parser(
#     user_id SERIAL PRIMARY KEY,
#     name VARCHAR(250) NOT NULL,
#     text VARCHAR(250) NOT NULL
# );'''
#
# # cursor.execute(create)
# # cursor.connection.commit()
#
#
#
#
# itc_page = requests.get(
#     url='https://itc.kg/index.html'
# ).text
#
# data = bs(itc_page,'html.parser')
#
# section = data.find('section', attrs={"id":"service"})
# all_col_md_4 = section.find_all('div', class_='col-md-4')
#
# for col in all_col_md_4:
#     name = col.h2.get_text()
#
#     definition = col.p.text.strip().split('\n')
#
#     if definition[-1] == 'Подробнее':
#         definition.pop(-1)
#
#     description = ' '.join([i.strip() for i in definition])
#
#
#     a = f'''INSERT INTO parser (name, text)
#         VALUES (\'{name}\', \'{description}\');'''
#
#     cursor.execute(a)
#     connection.commit()







#
# itc_page = requests.get(
#     url='https://itc.kg/index.html'
# )
#
# data = bs(itc_page.text, 'html.parser')
# info = data.find_all('div',class_='service-content')
#
#
# a=[]
#
# for i in (info[0:3]):
#     a.append(i.text)
#
# ux=a[0].split()
# java=a[1].split()
# python=a[2].split()
#
#
# ux1=[]
# java1=[]
# python1=[]
#
#
# d=' '.join(ux[1:-1])
# s=' '.join(java[1:-1])
# f=' '.join(python[1:-1])
#
# ux1.append(ux[0])
# ux1.append(d)
#
# java1.append(java[0])
# java1.append(s)
#
# python1.append(python[0])
# python1.append(f)
#
# print(ux1)
# print(python1)
# print(java1)
