import pyfirmata

board = pyfirmata.Arduino('COM3')

board.digital[2].write(0)