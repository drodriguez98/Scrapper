#   Queremos scrappear la página piensoymascotas.com

#   pip install requests bs4

import requests
from bs4 import BeautifulSoup

#   Función para obtener el precio. Indicamos la clase html que contiene el valor del precio.

def get_price(url):
    
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'html.parser')
    price_with_eur = soup.find("span", {"class": "tvcurrent-price"}).contents[0]

    return price_with_eur

#   Si no hay url se para el programa. Si hay url llamamos a la función get_price para obtener el precio.

while True : 

    url = input('¿De qué producto quieres saber el precio?')

    if url == '':

        break

    print(get_price(url))

    
