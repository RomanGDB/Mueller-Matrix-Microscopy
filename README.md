# Mueller Matrix Microscopy

<p align="center">
  <img src="https://github.com/user-attachments/assets/6645155c-c7f0-4c85-827c-15a9a16cb878" alt="Figura 1" width="350"/>
  <img src="https://github.com/user-attachments/assets/010148f0-9522-45eb-82d4-dc5af4be7078" alt="Figura 2" width="339.4"/>
</p>

## Resumen

La polarización es una propiedad fundamental de la luz que puede modelarse mediante cuatro números reales conocidos como parámetros de Stokes. Cuando la luz interactúa con un objeto, su estado de polarización se transforma a través de una función de transferencia conocida como matriz de Mueller. Esta matriz describe de forma completa las características polarimétricas del objeto, las cuales están directamente asociadas a sus propiedades físicas, principalmente de naturaleza mecánica. En los últimos años, surgió la imaginería polarimétrica de Mueller: una técnica capaz de medir las matrices de Mueller sobre un campo de visión acotado, permitiendo visualizar dichas características físicas en un mapa bidimensional.

## Materiales y metodología

El sistema diseñado consiste en un conjunto de piezas impresas en 3D y componentes ópticos que conforman un microscopio de matrices de Mueller con fines de investigación y uso en laboratorio. La iluminación está a cargo de un LED M405LP1 montado dentro de una carcasa, junto con dos lentes utilizadas como colector y condensador, y un polarizador lineal motorizado accionado por un motor de paso BYJ48. La muestra se posiciona sobre una platina impresa en 3D, sujeta a un stage XYZ manual. Un objetivo de microscopio captura la luz difractada por la muestra, la cual es proyectada sobre un sensor BFS-U3-51S5P-C mediante una lente de tubo, que en nuestro caso particular es una lente eléctrica [modelo]. Para reducir la altura total del sistema, se incorporó un espejo entre el objetivo y la cámara, redirigiendo el haz de luz sin comprometer la calidad de la imagen.

## Instalación

1) Instalar Visual C++ https://www.microsoft.com/es-es/download/details.aspx?id=48145
2) Descargar e instalar Python 3.10 https://www.python.org/downloads/
3) Descargar e instalar Visual Code Studio (VCS) https://code.visualstudio.com/
4) Descargar e instalar 'Git for Windows' desde VCS
5) Clonar https://github.com/RomanGDB/Mueller-Matrix-Microscopy/edit/main/
6) Instalar Spinnaker SDK https://www.teledynevisionsolutions.com/products/spinnaker-sdk/?model=Spinnaker%20SDK&vertical=machine%20vision&segment=iis
7) Instalar las librerías: numpy opencv-python simple-pyspin PyQt5
8) En caso de utilizar lente eléctrica, instalarla también.

## Contacto
No dudar en contactarme a mi email personal.
roman.demczylo@gmail.com
