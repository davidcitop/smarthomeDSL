import sys
import signal
from gpiozero import LED

led_sala = LED(17)
led_habitacion = LED(27)

def procesa(value_sala, value_habitacion):
    print value_sala

    if value_sala:
        led_sala.on()
        print "Encendido Sala"
    else:
        led_sala.off()
        print "Apagado Sala"

    if value_habitacion:
        led_habitacion.on()
        print "Encendido Habitacion"
    else:
        led_habitacion.off()
        print "Apagado Habitacion"        
    sys.stdout.flush()


try:
    print "Inicio"
    t.daemon=True
    t.start()
    signal.pause()
except (KeyboardInterrupt, SystemExit):
    raise
    print "Salida"
 
