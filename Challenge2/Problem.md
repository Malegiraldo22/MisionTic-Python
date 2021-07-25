# Reto 2: Multas por exceso de velocidad

Debido a la alta accidentalidad presentada en el último año en las carreteras del territorio nacional, el Gobierno Colombiano ha decidido implementar controles que permitan sancionara a los conductores que no respeten los límites de velocidad establecidos por los organismos de control. 
Con este fin, el Ministerio de Transporte ha decidido implementar radares de tramo en las carreteras con mayores índices de accidentalidad en el país. Los radares de tramo funcionan colocando dos cámaras en dos puntos alejados de una carretera con el fin de comprobar cuánto tiempo tarda un conductor recorrer dicho tramo. 
Estos radares no mide la velocidad de paso, sino el tiempo de paso representado como la velocidad media de un conductor en un trayecto con una longitud determinada. Formalmente, los radares de tramo se basan en el teorema de Lagrange (también conocido como el teorema de valor medio o de Bonnet-Lagrange), el cual nos dice que dice tenemos una función continua en un intervalo cerrado, y derivable en un intervalo abierto, entonces algún punto de ese intervalo abierto la función tendrá una derivada instantánea igual a la pendiente media de la curva en el intervalo cerrado.
Aunque estos conceptos pueden asustar en un principio, su interpretación es muy simple: si hacemos un viaje desde Bogotá a Tunja y nuestra velocidad media es de 100 Km/h, necesariamente en algún punto del trayecto nuestra velocidad habrá sido de 100 Km/h. Esto quiere decir que si la velocidad media supera la velocidad máxima permitida, gracias al teorema anterior, sabremos que en algún punto del trayecto se superó la velocidad máxima permitida. 
Por ejemplo, si colocamos las cámaras separadas 10 Km en un tramo cuya velocidad máxima es de 110 Km/h, y un conductor tarda 5 minutos en ser visto por la segunda cámara, sabremos que su velocidad media ha sido de 120 Km/h, y por tanto, en algún sitio ha superado la velocidad permitida.
Usted hace parte del equipo de desarrollo encargado de construir el software que procesará los datos registrados por las cámaras.Su misión es crear un programa en Python que permita saber si un conductor debe ser multado o no.

| Entrada | Salida |
|---------|--------|
|El programa recibirá 3 parámetros:|l programa imprimirá una línea indicando si el conductor debe ser multado o no. Se debe considerar lo siguiente:|
|La distancia en metros que separa dos cámaras.|Imprimirá OK si el conductor no superó la velocidad máxima.|
|La velocidad máxima permitida en ese trayecto en (Km/h).|Imprimirá MULTA si se superó la velocidad máxima en menos de un 25% de la velocidad permitida.
|El tiempo en segundos que tarda el conductor en recorrer el trayecto.|Imprimirá CURSO SENSIBILIZACION si la velocidad fue superada en un 25% o más de la velocidad permitida. En este caso además de la multa deberá realizar un curso de sensibilización.
||Debido a que los sistemas pueden fallar y registrar valores errados (por ejemplo, indicando que el tiempo que ha tardado el conductor es negativo). En esos casos, se deberá imprimir VALORES NEGATIVOS.|

# Challenge 2: Speeding tickets

Due to the high accident rate presented in the last year on the roads of the national territory, the Colombian Government has decided to implement controls that allow it to sanction drivers who do not respect the speed limits established by the control bodies.
To this end, the Ministry of Transportation has decided to implement section radars on the highways with the highest accident rates in the country. Section radars work by placing two cameras at two points away from a road in order to check how long it takes a driver to travel that section.
These radars do not measure the speed of passage, but the time of passage represented as the average speed of a driver on a path of a certain length. Formally, segment radars are based on Lagrange's theorem (also known as the mean value theorem or Bonnet-Lagrange), which tells us that it says we have a continuous function in a closed interval, and differentiable in an open interval , then some point of that open interval the function will have an instantaneous derivative equal to the mean slope of the curve in the closed interval.
Although these concepts can be scary at first, their interpretation is very simple: if we make a trip from Bogotá to Tunja and our average speed is 100 km / h, necessarily at some point along the way our speed will have been 100 km / h. This means that if the average speed exceeds the maximum allowed speed, thanks to the previous theorem, we will know that at some point along the way the maximum allowed speed was exceeded.
For example, if we place the cameras 10 km apart in a section whose maximum speed is 110 km / h, and a driver takes 5 minutes to be seen by the second camera, we will know that his average speed has been 120 km / h, and therefore, somewhere it has exceeded the allowed speed.
You are part of the development team in charge of building the software that will process the data recorded by the cameras. Your mission is to create a Python program that allows you to know if a driver should be fined or not.

| Entrance | Departure |
| --------- | -------- |
| The program will receive 3 parameters: | The program will print a line indicating whether the driver should be fined or not. The following should be considered: |
| The distance in meters that separates two cameras. | It will print OK if the driver did not exceed the maximum speed. |
| The maximum speed allowed on that journey in (Km / h). | It will print a FINE if the maximum speed was exceeded by less than 25% of the allowed speed.
| The time in seconds that the driver takes to cover the route. | It will print AWARENESS COURSE if the speed was exceeded by 25% or more than the allowed speed. In this case, in addition to the fine, you must take an awareness course.
|| Because systems can fail and register wrong values (for example, indicating that the time taken by the driver is negative). In those cases, NEGATIVE VALUES should be printed. 
