# MisionTic-Python
Un empleado desea conocer a cuánto dinero equivalen las retenciones exigidas por la ley en relación con los pagos que la compañía para la que trabaja le realiza mensualmente. 
Se ha firmado un contrato que le permite trabajar tres semanas al mes y 50 horas semanales. Con el propósito de verificar el valor total de los descuentos decide construir un programa en Python que le permita verificar el valor de su salario antes y después de realizar los descuentos. 
Después de consultar sobre la normatividad Colombiana y revisar con detalle su contrato laboral nota que debe tener en cuenta los siguientes aspectos:

* El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 180.
* Las horas extras se liquidan con un recargo del 45% sobre el valor de una hora normal.
* Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones de 1.5% del salario base.
* El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras, más las bonificaciones (si las hay).
* Se descontará 5.5% del salario total antes de descuentos para el plan obligatorio de salud.
* Se descontará 5% del salario total antes de descuentos para el aporte a pensión.
* Se descontará 5% del salario total antes de descuentos para caja de compensación.

Luego de considerar toda esta información, Camilo decide construir un programa que permita a cualquier empleado de la empresa verificar si los pagos son correctos.

|Entrada|Salida|
|-------|------|
|El programa recibirá 3 parámetros:
 El salario base del empleado.
 La cantidad de horas extras se representa a través de un número entero positivo. En caso de no realizar horas extras durante el mes, se ingresará el valor 0.
Si hubo bonificaciones se ingresará el valor 1, de lo contrario el valor 0.|
| El programa debe imprimir 2 valores:
El valor a pagar al empleado luego de realizar los descuentos de ley. El resultado debe imprimirse con un número decimal.
El salario total del empleado antes de descuentos. El resultado debe imprimirse con un número decimal. |

