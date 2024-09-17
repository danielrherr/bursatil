import pymysql
try:
	conexion = pymysql.connect(host='192.168.1.10', user='root', password='123456', db='SSBT',  port=3307)
	with conexion.cursor() as cursor:
			consulta = "SELECT * FROM pedidos;"
			cursor.execute(consulta)
 
			# Con fetchall traemos todas las filas
			peliculas = cursor.fetchall()
 
			# Recorrer e imprimir
			for pelicula in peliculas:
				print(pelicula)
    

except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)
conexion.close()	

def insertAny():
	try:
		with conexion.cursor() as cursor:
			consulta = "INSERT INTO peliculas(titulo, anio) VALUES (%s, %s);"
	    	#Podemos llamar muchas veces a .execute con datos distintos 		
			cursor.execute(consulta, ("Volver al futuro 1", 1985))
			cursor.execute(consulta, ("Ready Player One", 2018))		    
			cursor.execute(consulta, ("It", 2017))		    
			cursor.execute(consulta, ("Pulp Fiction", 1994))		    
		
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	
	conexion.commit()

