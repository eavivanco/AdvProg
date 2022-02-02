# Tarea 0: LegoSweeper :dancers:

## Consideraciones generales :bangbang:
* Al ejecutar el programa se muestra perfectamente el menú de inicio con los requerimientos pedidos, el programa no se rompe cuando el usuario comente un error al ingresar los datos pedidos.

* El tablero se crea de manera correcta, para determinar la cantidad de legos dentro del tablero se utilizó la fórmula descrita en el enunciado y se le aplicó la función ```ceil()``` de la librería ```math```.

* Luego de ejecutar el código se puede jugar de manera normal. Si el usuario pierde, se descubre todo el tablero, se arroja el puntaje y se acaba la partida. Si el usuario descubre todas las casillas sin legos el juego no termina, sin embargo, si el usuario hace una jugada más (descubriendo una casilla con lego), el juego se termina y se arroja el puntaje correspondiente a haber descubierto todas las casillas.

* Para lograr que el juego sea fluido, en vez de preguntar cada vez si quiere guardar la partida, se indica al usuario que en caso de querer hacerlo, debe ingresar el número 100 al momento dee ingresar la fila de la casilla que quiere descubrir. El tablero con números y legos se guarda sin problemas, sin embargo, no se guarda la cantidad de movimientos, el tablero del usuario ni el puntaje al terminar la partida.

* No es posible cargar una partida de manera correcta

## Cosas implementadas :smirk: y no implementadas :worried:

* **Inicio del programa**:
    * **Menu de inicio**: Completo
    * **Funcionalidades**: Parcialmente completo
    * **Puntajes**: Completo
    
* **Flujo de juego**:
    * **Menu de juego**: Completo
    * **Tablero**: Completo
    * **Legos**: Completo   
    * **Guardado de partida**: Parcialmente completo
    
* **Término del juego**:
    * **Fin del juego**: Parcialmente ompleto
    * **Puntajes**: Parcialmente completo
   
* **General**: Completo   

## Ejecución :running:
El módulo principal de la tarea a ejecutar es  ```Desarrollo_sabado_5.py```.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé es la siguiente:

1. ```random```: ```shuffle()```
2. ```math```: ```ceil()``` 
3. ```os``` : ```path.isfile()```

## Supuestos y consideraciones adicionales :flushed:
Los supuestos y consideraciones adicionales que son necesarios saber para corregir mi tarea son:

1. Ante un error en la respuesta del usuario en el menú, el programa pedirá una nueva respuesta hasta que obtenga una válida. En el caso del menú principal existe la opción de salir directamente, si hay una partida en curso, la manera de salir es guardar.

2. Se utilizó la función ```ceil()``` de la librería ```math``` para calcular los Legos que se ingresaron (como se sugiere en el enunciado), por lo que si el valor de L (explicado en el enunciado) es, por ejemplo, 5.00000000001, el tablero tendrá 6 Legos.

3. Al descubrir todas las celdas "seguras" el juego no termina, hace falta descubrir un Lego para que termine.

4. Al guardar una partida se guarda ```mi_tab```, lo que corresponde al tablero con todas las celdas descubiertas.

5. Pensé que la tarea se entregaba el domingo en la noche y supe el sábado a las 19:40 que me quedaban 20 minutos ```print("F")```


