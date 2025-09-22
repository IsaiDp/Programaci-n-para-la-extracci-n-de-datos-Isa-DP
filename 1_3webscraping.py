# Isai Dueñas Padron.
# 952, Meta 1.4 Analizar y Comprender Proceso de Extracción de Datos.

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os

def buscar_productos(articulo, num_paginas):

    # Configuración del driver de Selenium
    servicio = Service(ChromeDriverManager().install())
    opciones = Options()
    opciones.add_argument("--window-size=1920x1080")
    navegador = webdriver.Chrome(service=servicio, options=opciones)

    # Ir a Amazon
    navegador.get("https://www.amazon.com.mx")
    time.sleep(3)

    # Buscar el producto
    try:
        caja_busqueda = navegador.find_element(By.ID, "twotabsearchtextbox")
        caja_busqueda.clear()
        caja_busqueda.send_keys(articulo)
        boton_buscar = navegador.find_element(By.ID, "nav-search-submit-button")
        boton_buscar.click()
        time.sleep(3)
        print(f"Búsqueda realizada para: {articulo}")
    except:
        url = f"https://www.amazon.com.mx/s?k={articulo.replace(' ', '+')}"
        navegador.get(url)
        print(f"Usando búsqueda directa: {url}")

    # Hacer el Data frame al final
    df_final = pd.DataFrame()

    for pagina in range(num_paginas):
        time.sleep(3)
        html = navegador.page_source
        df_pagina = extraer_datos(html)
        df_final = pd.concat([df_final, df_pagina], ignore_index=True)

        # Ir a la siguiente página si existe
        if pagina < num_paginas - 1:
            try:
                siguiente = navegador.find_element(By.XPATH, "//li[@class='a-last']/a")
                siguiente.click()
            except:
                print("No hay más páginas")
                break

    navegador.quit()

    # Guardar CSV
    if not os.path.exists('datos'):
        os.makedirs('datos')
    df_final.to_csv("datos/productos_baterias_carro.csv", index=False, encoding="utf-8-sig")
    print("Datos guardados exitosamente")



def extraer_datos(html):
    """
    Extrae los datos de productos desde el HTML de la página de Amazon.
    Devuelve un DataFrame con Título, Precio, Rating y Envío.
    """
    datos = {
        "Titulo": [],
        "Precio": [],
        "Rating": [],
        "Envio": []
    }

    soup = BeautifulSoup(html, 'html.parser')
    resultados = soup.find_all("div", {"data-component-type": "s-search-result"})

    for item in resultados:
        # Título
        titulo = item.find("h2", class_="a-size-base-plus a-spacing-none a-color-base a-text-normal")
        if titulo:
            link = titulo.find("a")
            datos["Titulo"].append(link.text.strip() if link else titulo.text.strip())
        else:
            datos["Titulo"].append("Sin título")

        # Precio
        precio = item.find("span", class_="a-offscreen")
        datos["Precio"].append(precio.text.strip() if precio else "Sin precio")

        # Rating
        rating = item.find("span", class_="a-icon-alt")
        datos["Rating"].append(rating.text.strip() if rating else "Sin rating")

        # Envío
        envio_elemento = item.find("div", class_="a-row a-color-base udm-primary-delivery-message")
        datos["Envio"].append(envio_elemento.text.strip() if envio_elemento else "Sin información")

    return pd.DataFrame(datos)



if __name__ == '__main__':
    articulo = "baterias para carro"
    num_paginas = 2
    buscar_productos(articulo, num_paginas)