import sys
import numpy as np
import cv2
from simple_pyspin import Camera

sys.path.append('../')
from stokeslib.polarization_full_dec_array import polarization_full_dec_array
from stokeslib.calcular_stokes import calcular_stokes 

#Exposicion
exposure_time = 50000

# Numero de promedios
N = 1

def main():
    
    #Continua actualizando
    update = True
    		
    with Camera() as cam: # Acquire and initialize Camera

        #Exposicion
        cam.ExposureAuto = 'Off'
        cam.ExposureTime = exposure_time # microseconds
    	
        #Formato
        #cam.PixelFormat = "BayerRG8"

    	#Toma las fotos
        cam.start() # Start recording
    	
        while update:    
            #Capturar Stokes
            img = cam.get_array()

            #Medibles
            I90, I45, I135, I0 = polarization_full_dec_array(img)

            #Stokes
            S0, S1, S2 = calcular_stokes (I90, I45, I135, I0)

            #Imprimir vector de Stokes
            print('[ ' + str(int(np.mean(S0))) + ' , ' + str(np.mean(S1/S0)) + ' , ' +  str(np.mean(S2/S0)) + ' ]')


        cam.stop() # Stop recording

    return True

if __name__ == '__main__':

    if main():
        sys.exit(0)
    else:
        sys.exit(1)
