import requests
import simplejson as json

# Este script genera error desde Google, ya que no implementa autenticacion

# Que url visitar
# payload es la direccion web que se quiere acortar
# headers son los encabezados de la peticion, avisando que los datos
# enviados son de tipo json
# se emplea peticion POST mediante requests 
url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl" : "http://example.com"}
headers = {"Content-Type" : "application/json"}
r = requests.post(url, json=payload, headers=headers)

print(r.headers)
print(r.text)

