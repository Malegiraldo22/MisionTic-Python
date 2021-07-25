dist, vel_max, tim = input()
dist = int(dist)
vel_max = int(dist)
tim = int(dist)

if (dist < 0) or (vel_max < 0) or (tim < 0):
    print("VALORES NEGATIVOS")

tim_h = tim / 3600
dist_km = dist / 1000
vel_km = dist_km / tim_h

if vel_km < vel_max:
    print("OK")
elif (vel_km > vel_max) and (vel_km < (vel_max * 1.25)):
    print("MULTA")
elif vel_km >= (vel_max * 1.25):
    print("CURSO SENSIBILIZACION")