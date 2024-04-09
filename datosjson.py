import json
from datetime import datetime, timedelta

# Ruta del archivo JSON
ruta_archivo = "/home/devasc/labs/devnet-src/parsing/myfile.json"

try:
	# Abrir el archivo JSON
	with open(ruta_archivo) as archivo:
		# Cargar el contenido del archivo JSON en una variable
		ourjson = json.load(archivo)
		print("Archivo JSON cargado correctamente.")

        	# Verificar si la clave "expires_in" existe en el JSON
		if "expires_in" in ourjson:
            		# Obtener el valor de expiracion del JSON y convertirlo a entero
			tiempo_expiracion_segundos = int(ourjson["expires_in"])

			# Calcular la fecha y hora de expiración sumando el tiempo en segundos a la fecha y hora actual
			fecha_expiracion = datetime.now() + timedelta(seconds=tiempo_expiracion_segundos)

			tiempo_restante = fecha_expiracion - datetime.now()

			# Imprimir el valor del token ademas la fecha y hora de expiració
			print("Valor del token:", ourjson.get("access_token"))
			print("Fecha de expiración del token:", fecha_expiracion)
			print("Tiempo restante antes de que caduque el token:", tiempo_restante)
		else:
            		print("La clave 'expires_in' no está presente en el archivo JSON.")
except FileNotFoundError:
	print("El archivo JSON no se encontró en la ruta especificada.")
except json.JSONDecodeError:
	print("Error al decodificar el archivo JSON.")
