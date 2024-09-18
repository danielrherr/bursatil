import pymysql


class DataMenager:
	def __init__(self,host,user,password,db,port):
		try:
			self.connexion= pymysql.connect(host=host,user=user,password=password,db=db,port=port)
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print ("ocurrio un errro al conectar: ",e)
			self.connexion.close
		
	def insertAny(self,setencia):
		try:
			with self.connexion.cursor() as cursor:
				cursor.execute(setencia)
		except  (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("error insertando datos.")

#try:
#	conexion = pymysql.connect(host='192.168.1.10', user='root', password='123456', db='mercado',  port=3307)
#	with conexion.cursor() as cursor:
#			consulta = "SELECT * FROM pedidos;"
#			cursor.execute(consulta)
# 
#			# Con fetchall traemos todas las filas
#			peliculas = cursor.fetchall()
# 
#			# Recorrer e imprimir#
#			for pelicula in peliculas:
#				print(pelicula)
    

#except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
#	print("Ocurrió un error al conectar: ", e)
#conexion.close()	

#def insertAny(sentencia):
#	try:
#		with conexion.cursor() as cursor:
#			consulta = "INSERT INTO peliculas(titulo, anio) VALUES (%s, %s);"
#	    	#Podemos llamar muchas veces a .execute con datos distintos 		
#			cursor.execute(consulta, ("Volver al futuro 1", 1985))
#			cursor.execute(consulta, ("Ready Player One", 2018))		    
#			cursor.execute(consulta, ("It", 2017))		    
#			cursor.execute(consulta, ("Pulp Fiction", 1994))		    
		
#	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
#		print("Ocurrió un error al conectar: ", e)
	
#	conexion.commit()

