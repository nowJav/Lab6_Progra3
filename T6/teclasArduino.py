import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
print("Conectado")

#Variables---------------
#Variables
button = board.digital[4]
Led1 = board.digital[12]
Led2 = board.digital[8]

Led_Encendido = 0
button_enc = 0

#Iterador------------------
it = pyfirmata.util.Iterator(board)
it.start()
#-------------------------

def luz():
    encender = input("Ingrese AY para encender intermitentemente").upper()
    if encender == 'AJ':
        while True:
            Led1.write(1)
            Led2.write(1)    
            time.sleep(.5)
            Led1.write(0)
            Led2.write(0)
            time.sleep(.5)        
    else: 
        print("No son las Teclas correspondientes\n")

while True:
    luz()



