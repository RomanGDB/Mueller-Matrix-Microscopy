import sys
import numpy as np
import gzip
import os
import cv2

sys.path.append('../')
from camaralib.take_intensities import take_intensities
from stokeslib.acoplar_matriz import acoplar_matriz

#Directorio Raíz
os.chdir('..')

# Ruta carpeta en dónde guardar
IMG_SAVE_PATH = 'output/intensities/'  

if not os.path.exists(IMG_SAVE_PATH): 
    os.makedirs(IMG_SAVE_PATH)

# Exposicion
exposure_time = 5000

# Numero de promedios
N = 1

#Decimador 
decimador = 1

#Angulos de polarizacion de entrada
thetas_list = [0,30,60,90,120,150]
#thetas_list = [45,90,135,180]  

def main():
    #Nombre
    name = sys.argv[1]  

    #Toma vectores de Stokes
    I_stat = take_intensities(exposure_time, N, thetas_list)
    print(I_stat.shape)
    #Guarda numpy stokes comprimido
    print("Guardando imagen...")
    I_stat_img = acoplar_matriz(I_stat)
    cv2.imwrite(IMG_SAVE_PATH + 'I_' + name + '.png', I_stat_img)

    return True

if __name__ == '__main__':

    if main():
        sys.exit(0)
    else:
        sys.exit(1)
