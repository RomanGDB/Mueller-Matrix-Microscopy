import sys
import os

sys.path.append('../')
from raspberrylib.ejecutar_comando_ssh import ejecutar_comando_ssh

#Directorio de raíz
os.chdir('..')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python controlar_motores_ssh.py <motor> <movimiento>")
        print("Ejemplo: python controlar_motores_ssh.py X F  # Mueve el motor X hacia adelante")
        sys.exit(1)

    #Entrada tipo de motor y movimiento
    motor_input = sys.argv[1].upper()
    movimiento_input = sys.argv[2].upper()
    
    #Comando
    comando = f"cd /home/mwsi/Desktop/main && python motor_control.py {motor_input} {movimiento_input}"
    
    #Respuesta
    respuesta = ejecutar_comando_ssh(comando)
    print("Respuesta del servidor:")
    print("".join(respuesta))
