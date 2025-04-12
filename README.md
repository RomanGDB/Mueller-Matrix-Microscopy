# Mueller Matrix Microscopy

## Resumen

La polarización es una propiedad fundamental de la luz que puede modelarse mediante cuatro números reales conocidos como parámetros de Stokes. Cuando la luz interactúa con un objeto, su estado de polarización se transforma a través de una función de transferencia conocida como matriz de Mueller. Esta matriz describe de forma completa las propiedades polarimétricas del objeto, las cuales están directamente asociadas a sus propiedades físicas, principalmente de naturaleza mecánica. En los últimos años, surgió la imaginería polarimétrica de Mueller: una técnica capaz de medir las matrices de Mueller sobre un campo de visión acotado, permitiendo visualizar dichas características físicas en un mapa bidimensional.

## Materiales y metodología

<pre>
<p align="center">
  <img src="https://github.com/user-attachments/assets/9980bfc1-0515-4bea-8e9e-1b88e3ccab17" alt="Figura 1" width="500"/>
</p>
<p align="center"><b>Figura 1:</b> Diagrama del sistema.</p>
</pre>

El sistema diseñado consiste en un conjunto de piezas impresas en 3D y componentes ópticos que conforman un microscopio de matrices de Mueller con fines de investigación y uso en laboratorio. La iluminación está a cargo de un LED M405LP1 montado dentro de una carcasa, junto con dos lentes utilizadas como colector y condensador, y un polarizador lineal motorizado accionado por un motor de paso BYJ48 controlado por una Raspberry Pi. La muestra se posiciona sobre una platina impresa en 3D, sujeta a un stage XYZ manual. Un objetivo de microscopio captura la luz difractada por la muestra, la cual es proyectada sobre un sensor BFS-U3-51S5P-C mediante una lente de tubo, que en nuestro caso particular es una lente eléctrica [modelo]. Para reducir la altura total del sistema, se incorporó un espejo entre el objetivo y la cámara, redirigiendo el haz de luz sin comprometer la calidad de la imagen (ver Fig. 1).

Para medir los parámetros polarimétricos, seguimos el siguiente procedimiento. El polarizador del iluminador (generador) se rota en cuatro ángulos distintos: 0º, 45º, 90º y 135º. Para cada uno de estos estados de polarización del generador, se registran en la cámara cuatro imágenes correspondientes a los estados I₀, I₄₅, I₉₀ e I₁₃₅, que resultan de medir la luz difractada con un analizador orientado en esos mismos ángulos. En total, se obtienen 16 imágenes, las cuales se organizan en una matriz de intensidades de 4×4 (ver Fig. 2.a). A partir del formalismo de Stokes [1], se calculan los vectores de Stokes de entrada correspondientes a cada ángulo del generador. Esto proporciona cuatro estados de polarización de entrada y cuatro estados de polarización de salida. Con esta información, es posible estimar de forma robusta una matriz de Mueller 3×3, que representa la relación lineal entre los parámetros de Stokes de entrada y de salida (ver Fig. 2.b). Finalmente, utilizando una variante del algoritmo de descomposición de Lu-Chipman propuesta por Swami [2], se extraen tres propiedades polarimétricas fundamentales: la diatenuación, la retardancia lineal y el poder de depolarización (ver Fig. 2.c).

<pre>
<p align="center">
  <img src="https://github.com/user-attachments/assets/c3d254d9-ee3a-4968-9531-9013a7df6b32" alt="Figura 2" width="1000"/>
      a)                                          b)                                          c)
</p>  
<p align="center"><b>Figura 2:</b> Esquema de obtención de imágenes.</p>
</pre>

## Instalación

1) Instalar Visual C++  
https://www.microsoft.com/es-es/download/details.aspx?id=48145  
3) Descargar e instalar Python 3.10  
https://www.python.org/downloads/  
5) Descargar e instalar Visual Code Studio (VCS)  
https://code.visualstudio.com/  
7) Descargar e instalar 'Git for Windows' desde VCS  
8) Clonar github:  
https://github.com/RomanGDB/Mueller-Matrix-Microscopy/edit/main/  
10) Instalar Spinnaker SDK  
https://www.teledynevisionsolutions.com/products/spinnaker-sdk/?model=Spinnaker%20SDK&vertical=machine%20vision&segment=iis  
11) Instalar librerías  
numpy opencv-python simple-pyspin PyQt5 paramiko  
12) En caso de utilizar lente eléctrica  
Instalar Drivers https://www.optotune.com/downloads  
pip install git+https://github.com/OrganicIrradiation/opto.git  

## Referencias

[1] Edward Collett & Dennis H. Goldstein, *Polarized Light*, 3rd edition, CRC Press, 2010.  
[2] Mahesh Swami et al., *Polar decomposition of 3×3 Mueller matrix: a tool for quantitative tissue polarimetry*, Optics Express, 2006.

## Publicaciones relacionadas

Roman Demczylo & Ariel Fernández, *Single-shot 3×3 Mueller matrix microscopy with color polarization encoding*, Optics Letters, 2024.  

## Contacto
No dudar en contactarme a mi email personal:  
roman.demczylo@gmail.com
