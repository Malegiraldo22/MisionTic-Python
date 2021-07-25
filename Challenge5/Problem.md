# Reto 5: Inventario para la tienda de Juan

La tienda de Juan vende diferentes productos, usualmente frutas, dulces y algunos tipos de carne. Con el propósito de mejorar el control sobre las ventas y el inventario de la tienda, Juan decide construir una aplicación que le permita almacenar la información de los productos y realizar algunos cálculos sobre los datos.
En la primera parte del reto se debe construir una base de datos que almacene la información de los productos disponibles en la tienda. Debido a que Juan no cuenta con un servidor de base de datos, solicita que temporalmente la base de datos sea representada mediante un diccionario de Python llamado productos que tendrá por llave el código del producto y por valor una lista formada por los atributos: nombre, precio e inventario. La Tabla 1 presenta los productos disponibles a la fecha.

|Código|Nombre|Precio|Inventario|
|------|------|------|----------|
|1|Naranjas|7000.0|35|
|2|Limones|2500.0|15|
|3|Peras|2700.0|65|
|4|Arandanos|9300.0|34|
|5|Tomates|2100.0|42|
|6|Fresas|9100.0|20|
|7|Helado|4500.0|41|
|8|Galletas|500.0|8|
|9|Chocolates|4500.0|80|
|10|Jamon|17000.0|48|

Para simular de una manera más realista la base de datos, es necesario construir 3 funciones que representen las operaciones de: AGREGAR, ACTUALIZAR y BORRAR los productos disponibles. Se debe implementar una función independiente por cada una de las acciones mencionadas. En este caso, para poder realizar las operaciones de ACTUALIZAR o BORRAR es necesario especificar todos los atributos del producto.

Adicionalmente, Juan está interesado en analizar los datos de los productos disponibles y conocer: el nombre del producto con el precio mayor; el nombre del producto con el precio menor; el promedio de precios de todos los productos y el valor total del inventario a la fecha. Este último se obtiene multiplicando el precio de cada producto por el inventario disponible y luego sumando todos los resultados. Por ejemplo, al calcular estos 4 valores para los datos disponibles en la Tabla 1 obtendríamos :

* Producto precio mayor: Jamon
* Producto precio menor: Galletas
* Promedio de precios: 5920.0
* Valor del inventario: 2408900.0

|Entrada|Salida|
|-------|------|
|Cada uno de los casos de prueba estará compuesto por dos líneas.|La salida estará representada por una única línea formada por cuatro valores:|
|La primera línea estará formada por una cadena de texto que identifica la operación a realizar. En este caso, las operaciones validas son: ACTUALIZAR, BORRAR, AGREGAR.|Nombre del producto con el precio mayor. Nombre delproducto con el precio menor. Promedio de precios. Valor del inventario.|
|La segunda línea estará formada por 4 valores (código, nombre, precio, inventario) que representan el producto sobre el cual se quiere realizar la operación.| Estos 4 valores deben imprimirse después de realizar las operaciones solicitadas en la entrada de datos. Los valores numéricos deben imprimirse con un número decimal.|
|En el caso de la operación ACTUALIZAR la segunda línea debe contener el código y los nuevos valores del producto.|En caso de solicitar ACTUALIZAR o BORRAR un producto que no existe (es decir, que el código del producto no se encuentra en la base de datos), se debe imprimir 'ERROR'.|
|En el caso de la operación BORRAR se deben especificar todos los atributos del producto a eliminar.|En caso de solicitar AGREGAR un producto cuyo código ya existe en la base de datos se debe imprimir 'ERROR'.|

# Challenge 5: Inventory for Juan's store

Juan's store sells different products, usually fruits, sweets, and some types of meat. In order to improve control over the store's sales and inventory, Juan decides to build an application that allows him to store product information and perform some calculations on the data.
In the first part of the challenge, a database must be built that stores the information of the products available in the store. Since Juan does not have a database server, he requests that the database be temporarily represented by a Python dictionary called products, which will have the product code as a key and a list made up of attributes: name, as a value. price and inventory. Table 1 presents the products available to date.

| Code | Name | Price | Inventory |
| ------ | ------ | ------ | ---------- |
| 1 | Oranges | 7000.0 | 35 |
| 2 | Lemons | 2500.0 | 15 |
| 3 | Pears | 2700.0 | 65 |
| 4 | Blueberries | 9300.0 | 34 |
| 5 | Tomatoes | 2100.0 | 42 |
| 6 | Strawberries | 9100.0 | 20 |
| 7 | Ice cream | 4500.0 | 41 |
| 8 | Cookies | 500.0 | 8 |
| 9 | Chocolates | 4500.0 | 80 |
| 10 | Ham | 17000.0 | 48 |

To simulate the database in a more realistic way, it is necessary to build 3 functions that represent the operations of: ADD, UPDATE and DELETE the available products. A separate function must be implemented for each of the actions mentioned. In this case, in order to perform the UPDATE or DELETE operations, it is necessary to specify all the attributes of the product.

Additionally, Juan is interested in analyzing the data of the available products and knowing: the name of the product with the highest price; the name of the product with the lowest price; the average prices of all products and the total inventory value to date. The latter is obtained by multiplying the price of each product by the available inventory and then adding all the results. For example, when calculating these 4 values ​​for the data available in Table 1 we would obtain:

* Product higher price: Ham
* Product lower price: Cookies
* Average prices: 5920.0
* Inventory value: 2408900.0

| Entry | Exit |
| ------- | ------ |
| Each of the test cases will be made up of two lines. | The output will be represented by a single line made up of four values: |
| The first line will consist of a text string that identifies the operation to be performed. In this case, the valid operations are: UPDATE, DELETE, ADD. | Name of the product with the highest price. Name of the product with the lowest price. Average prices. Inventory value.
| The second line will be made up of 4 values (code, name, price, inventory) that represent the product on which the operation is to be carried out. | These 4 values should be printed after performing the requested data entry operations. Numeric values ​​must be printed with a decimal number.
| In the case of the UPDATE operation, the second line must contain the code and the new values of the product. | In case of requesting UPDATE or DELETE a product that does not exist (that is, the product code is not in the database data), it should print 'ERROR'.
| In the case of the DELETE operation, all the attributes of the product to be eliminated must be specified. | In case of requesting ADD a product whose code already exists in the database, 'ERROR' must be printed. | 
