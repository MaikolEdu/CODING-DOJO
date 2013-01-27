class Romanos:
	resultado=""
	def ingresar(yo):
		numero= raw_input('\tIngresar numero :')
		yo.numero= int (numero)		

	def caso1(yo,letra,num):
		return letra*num
	def caso2(yo,letra,num,letra2):
		if num==4:			
			return letra+letra2
		return letra+"X"
	def caso3(yo,letra,numero):
		if numero==5:
			return letra
		numero-=5
		return letra + yo.caso1("I",numero)

	def proceso(yo):
		numero= yo.numero
		if yo.numero==4 or yo.numero==9:
			yo.resultado+=yo.caso2("I",numero,"V")
		elif yo.numero >= 5:
			yo.resultado+=yo.caso3("V",numero)
		elif yo.numero>=1:
			yo.resultado+=yo.caso1("I",numero)	
		print yo.resultado

	def __init__(yo):
		yo.ingresar()
		yo.proceso()

objeto = Romanos()
