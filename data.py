from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient  # Paquete para MongoDB
from pymongo.server_api import ServerApi
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')  # Ignora errores SSL
chrome_options.add_argument('--ignore-ssl-errors')


# Configuración de Selenium y ChromeDriver
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("ChromeDriver inicializado correctamente")
except Exception as e:
    print(f"Error al iniciar ChromeDriver: {e}")
    exit()  # Salir si no se puede iniciar el navegador

# URL de la página
url = "https://rava.com/cotizaciones/bonos"

# Navegar a la página
try:
    driver.get(url)
    print("Página cargada correctamente")
except Exception as e:
    print(f"Error al cargar la página: {e}")
    driver.quit()
    exit()  # Salir si no se puede cargar la página

# Esperar un momento para que la página cargue completamente
time.sleep(10)  # Ajusta el tiempo si es necesario

# Obtener el contenido de la página
try:
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')

    # Encontrar la tabla de cotizaciones de bonos
    table = soup.find('table')  # Ajustar el selector según sea necesario

    if table is None:
        print("No se encontró la tabla. Verifica el selector.")
    else:
        # Extraer el encabezado de la tabla y limpiarlo
        headers = [header.text.strip().replace('\n', '').replace('\t', '').replace('▼ ▲', '') for header in table.find_all('th')]
        print("Encabezados de la tabla:", headers)
        
        # Extraer los datos de la tabla
        bonos = []
        for row in table.find_all('tr')[1:]:  # Saltar el encabezado
            columns = row.find_all('td')
            if len(columns) == len(headers):
                bono = {headers[i]: columns[i].text.strip() for i in range(len(headers))}
                bonos.append(bono)
            else:
                print("Fila no válida o con columnas insuficientes:", [col.text for col in columns])

        # Intentar insertar los datos en MongoDB
        try:
            if bonos:
               # collection.insert_many(bonos)
                print(f'Se han insertado {len(bonos)} documentos en MongoDB. {bono}')
        except Exception as e:
            print(f"Error al insertar datos en MongoDB: {e}")

        # Mostrar los datos extraídos (opcional)
        for bono in bonos:
            stringInsert = f'INSERT INTO cotizaciones (Especie,Cotizacion Fecha,Hora) values ({bono["Especies"]},{bono["Ultimo"]},{bono["Hora"]})'
            print(f'Especie: [{bono["Especie"]}]   Cotización: [{bono["Último"]}] Hora:[{bono["Hora"]}]  Fecha: [{bono["Fecha"]}]')
except Exception as e:
    print(f"Error al procesar los datos de la página: {e}")

# Cerrar el navegador
driver.quit()
