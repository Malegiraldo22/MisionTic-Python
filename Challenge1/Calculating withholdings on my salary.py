print(""""
Ingrese el salario base, las horas extra y las bonificaciones
En caso de no tener horas extra y bonificaciones ingresar 0
""")

salario_base, horas_extra, bonificaciones = input().split()

salario_base = float(salario_base)
horas_extra = float(horas_extra)
bonificaciones = float(bonificaciones)

valor_hora = salario_base / 180
hora_extra = valor_hora * 1.45 * horas_extra

if bonificaciones == 1:
    bonificacion = salario_base * 0.015
else:
    bonificacion = 0


salario_neto = salario_base + hora_extra + bonificacion
salud = salario_neto * 0.055
pension = salario_neto * 0.05
compensacion = salario_neto * 0.05
salario_total = salario_neto - salud - pension - compensacion

print(round(salario_total,1), round(salario_neto,1))