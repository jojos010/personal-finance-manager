#Este va a ser mi primer proyecto en python, primeramente mi idea sera crear las siguientes funciones:
#Debe tener un login, con usuario y contraseña
#Mostrar un menu de opciones
#Guardar datos incluso al salir del programa
#
#	LOGIN
#	1.Total del saldo actual
#	2.Ingresos:
#		A su vez cada ingreso debera tener su:monto,fecha,categoria y descripcion
#	3.Gastos
#		Gastos fijos: Comida,alquiler,internet
#		Gastos extra: ropa, productos de aseo, corte de pelo
#	4.Balance
#       Diferencia entre ingresos y egresos
#   5.Reportes
#		Total gastado
#			Por categoria
#		Total ingresado
#			Por categoria
#		Gastos por Dia, Semana, Mes
#			Mayores gastos
#		Ahorro
#			Dinero en cuenta bancaria
#	6.Salir
login_correcto = False
while not login_correcto:
	usuario = "jojos"
	contraseña = "1234"
	login_usuario = input("Ingrese su usuario: ")
	login_contraseña = input("Ingrese su contraseña: ")
	if usuario == login_usuario and contraseña == login_contraseña:
		print("\n")
		print(f"{"="*10} Hola Jos!, Bienvenido {"="*10}")
		login_correcto = True
	else:
		print("\n")
		print(f"{"%"*10} Datos incorrectos {"%"*10}")
		print("\n")
		print("++Intente de nuevo...++")
	
