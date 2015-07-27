import mysql.connector

config_mysql = {
  'user': 'Azalia',
  'password': 'dylan2109',
  'host': '127.0.0.1',
  'database': 'practica',
  'raise_on_warnings': True,
}

conex = mysql.connector.connect(**config_mysql)

conex.close()

try:
  conex = mysql.connector.connect(config_mysql)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Escribiste algo mal, verifica")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("La base de datos a la que intentas acceder no existe")
  else:
    print(err)
else:
  conex.close()
