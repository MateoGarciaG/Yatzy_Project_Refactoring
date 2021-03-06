# REFLEXIONES YATZY KATA REFACTORING

## Reflexión General:
Este kata me ha permitido seguir practicando el proceso adecuado del TDD como también a examinar y evaluar si el código escrito se podría refactorizar, más de allá de de tener un código más refactorizado es la utilidad de poder identificar como se puede llegar a tener un código más optimo y organizado y que siga unas convenciones y buenas practicas.
## Code Smells Identificados:
Los Code Smells que he identificado en este kata y de los cuales realice refactorización y de acuerdo a la CheckList fueron:

### Code Smells a nivel de rutina y Casos TEST:
File test_yatzy: Toda la refactorización se llevo a cabo en la Branch: feature-tests
1. Nombres de funciones/rutinas con los casos test según su categoría o método con malas practicas, es decir, los nombres de la mayoria de las rutinas de los casos test no tienen buenos nombre según lo que establece pep8
2. No había orden de los casos test según la funcionalidad de cada método de la Clase Yatzy, es decir, no había un orden concreto para poder identificar de mejor manera cada función con los casos test. Donde recordemos que en el juego Yatzy tenemos una separación entre los casos test que suman una determinada cantidad de puntos y los casos test que solo suman la cantidad de dados según el número del dado que haya.
3. Al momento de declarar los ASSERTS de cada una de las funciones que contienen los casos test, no hay un orden establecido sobre como debe declararse, a pesar de que no influye en el flujo de ejecución de los casos test mediante pytest, es mejor tener un orden en la declaración de los ASSERTS, por ejemplo, primero colocar el resultado del método y si es == al resultado que nosotros queremos que sea.
4. En aquellos casos test donde tenemos métodos que queremos que el resultado sea una cantidad de puntos específica como poker, smallStraight, etc. En algunos casos test se repite este valor específico teniendo en cuenta que anteriormente ya estaba definido en una variable.

### Code Smells a nivel de Clase, rutina/método y declaración:
yatzy.py:
1. Obsevando los casos test y la funcionalidad de la Clase Yatzy, vemos que la mayoría de métodos son estaticos, lo que quiere decir que no hay muchos métodos los cuales se quieran encapsular por ejemplo: fives() o que por lo menos para las funcionalidades basicas para que funcione el juego de Yatzy, hay necesidad de tener método estaticos, debido a que los casos test están evaluando un solo juego actual de Yatzy, ya que si creamos varios objetos para cada función con los casos test, veremos que al final el total de puntos no se podría calcular, por lo cual es mejor convertir todos los métodos de la clase Yatzy en estaticos para tener control sobre el resultado total de un jugador y ver si gano o no.
2. Hay algunas rutinas que no siguen la convención de nombre de rutina de PEP8
3. A pesar de que el estandar del juego de Yatzy son 5 dados, esto no es una regla definitiva. Por lo cual si tenemos en cuenta esto, los métodos de la clase Yatzy no están adaptados para recibir más de 5 párametros.
4. Hay muchos métodos donde se crea un array y en vez de usar una estructura más optima, se asigna el valor al elemento de ese array uno por uno.
5. Hay algunos métodos que tienen demasiados condicionales los cuales se pueden refactorizar.


## Preguntas de Reflexión:

### ¿Cuánto código duplicado hay en tu solución? ¿Y en tus casos test?
Respecto a los casos test debido a que cada caso test es único relacionado especificamente a un método sea o no estático de la clase Yatzy, y viendo que están separados en sus debidas funciones test según el método. Creo que está bien.
Respecto a la clase Yatzy en la mayoría de métodos tienen su propia funcionalidad obviamente a pesar de que en la mayoría de ellos se siguio una forma de refactorización, ya sea por el *args o porque se ordeno está tupla para optimizar el loop for.

### ¿Escribiste una lista de casos test antes de comenzar?
Si, decidí crear dos branch: feature-tests. La cual era especificamente para refactorizar los casos test y agregar nuevos casos test. Y otra branch llamada: feature-class-yazty. La cual era especificamente para refactorizar la Class Yatzy.
Donde primero empece con la branch feature-tests para seguir el proceso de TDD antes de pasar a refactorizar o mirar el código de la Class Yatzy. Cuando ya tenía refactorizada ambas branchs, decidí unirlas mediante git merge a la branch develop, y de allí observar si todo funcionaba, todo funcionaba más allá de algún que otro error por una variable en un método al momento de refactorizar, pero no mucho más.
### ¿Cómo decidiste el orden en el que implementar los casos test? 
Decidí que el orden de los casos test debían ser desde aquellos puntajes del 1-6, para despues avualuar los casos test de los pair, straight, full_house, etc. Donde están dividos en sus propias funciones test según el método a evaluar en los casos test. Y dentro de cada función poner los casos test más comunes según el total de puntos que podría dar, no según la posición de los dados sino solamente la puntuación.

