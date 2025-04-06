import requests
from bs4 import BeautifulSoup
import time

# URL de la página que queremos scrapear
url = 'https://listado.mercadolibre.com.ec/mac?sb=rb#D%5BA:mac%5D'  # Reemplaza con una URL real

# Realizamos la petición HTTP
try:
    response = requests.get(url)
    response.raise_for_status()  # Lanza un error si la petición falla
    # Parseamos el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Encuentra todos los elementos que contengan los títulos de noticias
    # (Necesitarás inspeccionar la página para saber los selectores correctos)
    news_titles = soup.find_all('a', class_='poly-component__title')  # Ajusta según la página
    
    # Imprimimos los títulos encontrados
    print("Títulos de noticias encontrados:")
    lista={}
    for i, title in enumerate(news_titles, 1):
        print(f"{i}. {title.get_text(strip=True)}")
        lista[f'item{i}']=title.get_text(strip=True)
    
    print(lista['item1'])
except requests.exceptions.RequestException as e:
    print(f"Error al realizar la petición: {e}")
except Exception as e:
    print(f"Ocurrió un error: {e}")