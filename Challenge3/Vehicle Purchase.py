n = int(input())

catalogo = []
capital = 12000
total = []

for i in range(n):
    carro = input().split()
    catalogo.append(carro)

for carro in catalogo:
    cc = int(carro[0])
    año = int(carro[1])
    km = int(carro[2])
    consumo = int(carro[3])
    precio = int(carro[4])
    

    if ((cc >= 1200) and (cc < 3600)) and (año >= 2018) and \
          (km <= 30000) and (consumo < 35) and \
          ((precio > 13500) and (precio <= 26000)):
        total.append(precio - capital)
    else:
        total.append("NO DISPONIBLE")
    
contador = 0
for i in total:
    if i == "NO DISPONIBLE":
        contador += 1
    else:
        print(i)
    
if contador == len(total):
    print("NO DISPONIBLE")