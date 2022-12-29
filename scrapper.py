#   Página que scrappeamos --> piensoymascotas.com

#   Instalamos librerías --> pip install requests bs4

#   Las importamos 

import requests
from bs4 import BeautifulSoup

#   Función para obtener el precio

def get_price(url):
    
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'html.parser')
    price_with_eur = soup.find("span", {"class": "tvcurrent-price"}).contents[0]

    return price_with_eur

#   Si no hay url se para el programa, si hay url llamamos a la función para obtener el precio

while True : 

    url = input('¿De qué producto quieres saber el precio?')

    if url == '':

        break

    print(get_price(url))

    