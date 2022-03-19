import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
print("Conectado")

#Variables
button = board.digital[4]
Led1 = board.digital[12]
Led2 = board.digital[8]

Led_Encendido = 0
button_enc = 0

it = pyfirmata.util.Iterator(board)
it.start()
button.mode = pyfirmata.INPUT

while True:

    button_state = button.read()
    if button_state != button_enc:
        if button_state is False:
            
            Led1.write(0)
            Led2.write(0)
            Led_Encendido +=1
            time.sleep(.05)
            print("Pulsado")
            if Led_Encendido == 2:
                Led1.write(1)
                time.sleep(2)
                Led1.write(0)
            elif Led_Encendido == 4:
                Led2.write(1)
                time.sleep(2)
                Led2.write(0)
                Led_Encendido = 0
                

    button_enc = button_state


            






