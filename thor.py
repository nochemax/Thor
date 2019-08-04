# Name_Programa: Thor
# Name: Smp_A
# Descripcion: Descifra archivos gpg 
# Modo de ataque: Fuerza bruta
# Recomendaciones: usar crunch para crear diccionarios
# version: 0.01
# Python

from io import open
import os
import subprocess 


archivo_texto=""
file=""
cnt=0
captura="no_ok"
linea=""
line=""	
out=""
fichero=""

os.system('clear') 
print("\033[1;31;1m ")
os.system('figlet  Thor')
print("\033[1;33;1m ")
print("             	  Smp_A")
print("\033[1;37;1m ")
print("")

archivo_texto=raw_input("Introduzca Ruta File key.txt: ")
file=raw_input("Introduzca Ruta File gpg: ")

while captura=="no_ok":	

	with open(archivo_texto,'r') as fichero:
			
		for linea in fichero:
				
			line=(str(linea.rstrip()))
			cnt=cnt+1

			print("---Date_Attack---" +str(cnt))
			print(file)
			print(line)
			print("-----------------")
			print("")
				
			print("---Date_out_Attack---")
			out = os.system('gpg --pinentry-mode loopback --batch --yes --passphrase '+line+' -d '+file)
			print("")
			print(str(out))
			print("---------------------")
					
			if (out == 0):					
				print("")
				print("\033[1;31;1m ")
				os.system('figlet  Smp_A')
				print("\033[1;36;1m ")
				print("		>$$$$$$$$$$$$$$$$$$$$$$$$$$$<")
				print("\033[1;37;1m ")
				print("		  Tengo la clave correcta")
				print("		  Numero de intentos:"+str(cnt))
				print("		  La clave es: "+line)
				print("\033[1;36;1m ")
				print("		>$$$$$$$$$$$$$$$$$$$$$$$$$$$<")
				captura="ok"
				print("\033[1;37;1m ")
				print(captura)
				break

# crunch [numero minimo de digitos]  [numero maximo de digitos] [carateres] [-o /ruta/nombrearchivo.txt]
# Ejemplo
#archivo_texto = "/root/Documentos/RetoCrypto/key.txt"
#file = "/root/Documentos/RetoCrypto/comprobacion.txt.gpg"
