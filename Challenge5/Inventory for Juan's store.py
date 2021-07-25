productos = {
    1: ["Naranjas", 7000.0, 35],
    2: ["Limones", 2500.0, 15],
    3: ["Peras", 2700.0, 65],
    4: ["Arandanos", 9300.0, 34],
    5: ["Tomates", 2100.0, 42],
    6: ["Fresas", 9100.0, 20],
    7: ["Helado", 4500.0, 41],
    8: ["Galletas", 500.0, 8],
    9: ["Chocolates", 4500.0, 80],
    10: ["Jamon", 17000.0, 48] 
}

def AGREGAR(codigo, nombre, precio, inventario):
    if codigo in productos.keys():
        print("ERROR")
    else:
        productos[codigo] = [nombre, precio, inventario]
        analisis()

def ACTUALIZAR(codigo, nombre, precio, inventario):
    if codigo not in productos.keys():
        print("ERROR")
    else:
        productos[codigo] = [nombre, precio, inventario]
        analisis()

def BORRAR(codigo, nombre, precio, inventario):
    if codigo not in productos.keys():
        print("ERROR")
    else:
        del productos[codigo]
        analisis()

def analisis():
    prod = []
    precios = []
    unidades = []
    total = 0

    for key in productos.keys():
        prod.append(productos[key][0])
        precios.append(productos[key][1])
        unidades.append(productos[key][2])
        pre = productos[key][1]
        und = productos[key][2]
        sub_total = pre * und
        total += sub_total

    prod_mayor = prod[precios.index(max(precios))]
    prod_menor = prod[precios.index(min(precios))]
    prod_prom = round(sum(precios) / len(precios), 1)
    val_inv = total

    print(prod_mayor, prod_menor, prod_prom, val_inv)

operacion = input().lower()
codigo, nombre, precio, inventario = input().split()
codigo = int(codigo)
precio = float(precio)
inventario = int(inventario)

if operacion == "agregar":
    AGREGAR(codigo, nombre, precio, inventario)
elif operacion == "actualizar":
    ACTUALIZAR(codigo, nombre, precio, inventario)
elif operacion == "borrar":
    BORRAR(codigo, nombre, precio, inventario)