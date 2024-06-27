import json
from urllib.request import urlopen
from datetime import datetime, timedelta
import os

# Obtener la fecha actual
current_date = datetime.now()

# Sumar un día a la fecha actual
next_date = current_date + timedelta(days=1)

# Formatear la nueva fecha a string
next_date_str = next_date.strftime('%Y-%m-%d')
print(next_date_str)

# URL con la nueva fecha
url = f'https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=ha.ruiz@duocuc.cl&pass=Ruizharry32.&function=GetSeries&timeseries=F073.TCO.PRE.Z.D&firstdate={next_date_str}&lastdate={next_date_str}'

response = urlopen(url)
data_bytes = response.read()
data_str = data_bytes.decode('utf-8')
data_dict = json.loads(data_str)

# Obtener el valor del dólar
dolar = float(data_dict["Series"]["Obs"][0]["value"])

# Guardar el valor del dólar en un archivo JSON en la carpeta estática
static_path = os.path.join(os.path.dirname(__file__), 'static', 'js', 'dolar.json')
with open(static_path, 'w') as json_file:
    json.dump({"dolar": dolar}, json_file)

print(f"Archivo guardado en: {static_path}")
