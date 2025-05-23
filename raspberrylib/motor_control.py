import RPi.GPIO as GPIO
import time

# Diccionario con pines de GPIO para cada motor
motores = {
    "X": {
        "motor_pins": {
            "motor_pin1": 17,
            "motor_pin2": 22,
            "motor_pin3": 2,
            "motor_pin4": 3},
        "step_num": 2*10,
    },
    "Y": {
        "motor_pins": {
            "motor_pin1": 26,
            "motor_pin2": 16,
            "motor_pin3": 20,
            "motor_pin4": 21, },
        "step_num": 2*10,
    },
    "T": {
        "motor_pins": {
            "motor_pin1": 19,
            "motor_pin2": 13,
            "motor_pin3": 6,
            "motor_pin4": 5, },
        "step_num": (512*68)//360, #512 por vuelta
    }
}

# Definición de la secuencia de pasos para cada motor
sequence_nema = [[1, 0, 1, 1],
                 [0, 0, 1, 0],
                 [0, 1, 0, 0],
                 [1, 1, 0, 1]]

sequence_theta = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]]

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for motor, motor_info in zip(motores.keys(), motores.values()):
    pins = motor_info['motor_pins']
    for pin in pins.values():
        GPIO.setup(pin, GPIO.OUT)


# Función para avanzar el motor un paso
def step_forward(motor):
    pins = motores[motor].get('motor_pins')
    sequence = sequence_nema if motor == "X" or motor == "Y" else sequence_theta
    for step in sequence:
        GPIO.output(pins["motor_pin1"], step[0])
        GPIO.output(pins["motor_pin2"], step[1])
        GPIO.output(pins["motor_pin3"], step[2])
        GPIO.output(pins["motor_pin4"], step[3])
        time.sleep(0.01)


# Función para retroceder el motor un paso
def step_backward(motor):
    pins = motores[motor].get('motor_pins')
    sequence = sequence_nema if motor == "X" or motor == "Y" else sequence_theta
    for step in reversed(sequence):
        GPIO.output(pins["motor_pin1"], step[0])
        GPIO.output(pins["motor_pin2"], step[1])
        GPIO.output(pins["motor_pin3"], step[2])
        GPIO.output(pins["motor_pin4"], step[3])
        time.sleep(0.01)


# Función para controlar los motores
def controlar_motores(motor_input, movimiento_input, steps):
    try:
        if motor_input not in motores or movimiento_input not in ["F", "B"]:
            raise ValueError("Motor o movimiento no válido.")

        motor = motor_input
        movimiento = movimiento_input
        if movimiento == "F":
            for _ in range(steps):
                step_forward(motor)
        elif movimiento == "B":
            for _ in range(steps):
                step_backward(motor)

    except KeyboardInterrupt:
        # Detener el motor si se interrumpe manualmente con Ctrl+C
        GPIO.cleanup()


# Ejemplo de uso con valores proporcionados desde línea de comandos
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Uso: python main.py <motor> <movimiento> <angle>")
        print("Ejemplo: python main.py T F angle  # Mueve el motor X hacia adelante")
        sys.exit(1)

    #Entradas
    motor_input = sys.argv[1].upper()
    movimiento_input = sys.argv[2].upper()
    cantidad = float(sys.argv[3].upper())

    #Pasos
    if motor_input in ['X', 'Y']:
        steps = int(50 * cantidad)        # mm
    elif motor_input == 'T':
        steps = int((512 * cantidad) / 360) # grados

    #Controlar motores
    controlar_motores(motor_input, movimiento_input, steps)
