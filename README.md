# MII_IOTA_PDF

## Objetivo
Proyecto de la asignatura 'Comunicación y Divulgación de la Ciencia y la tecnología' del Master de Ingeniería Industrial de la UPM. En este repositori se muestra un breve ejemplo de la capacidad de transmisión de archivos a través de Iota.

## Requierements
API de IOTA para python:
 *pip install PyOTA*

## Cómo funciona
Es un programa muy básico. El script *sending.py* permite enviar un archivo, actualmente apuntando a 0.txt; el script *receiving.py* permite replicar ese archivo en la misma carpeta.

### Instrucciones
    - Se puede modificar, en *sending.py*, la dirección (*address*) y etiqueta (*tag*) por cualquiera que cumpla los requisitos.
    - Se puede enviar cualquier tipo de archivo siempre que se especifique su nombre correctamente en *sending.py*:
    ```f = open("0.txt", "rb")```
    **Observación**: los archivos se convierten de *base64* a un *TryteString*. El tamaño por transacción se encuentra limitado a 2187 caracteres; grandes archivos requerirán tantas transacciones que es probable que el
    nodo que las está uniendo al *tangle* rechace la solicitud.
    - Cuando se envía un archivo se deben apuntar los siguientes parámetros:
    ![alt text](https://github.com/fjaviergb/MII_IOTA_PDF.git/images/input.PNG)
    - Estos parámetro se introducirán en *receiving* líneas 9 y 12.

