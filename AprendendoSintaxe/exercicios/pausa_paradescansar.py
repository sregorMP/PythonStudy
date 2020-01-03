# Um video a cada tempo de estudo
import webbrowser
import time

intervalos = 2 
contador  = 0 
print('programam controle de descanso ativado')

while contador < intervalos: 
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=0m4-u8h_vj4')
    contador = contador + 1    