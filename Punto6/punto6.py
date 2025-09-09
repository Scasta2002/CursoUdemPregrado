def simular_ahorro(ahorro_mensual, meses, meta):
    total = 0
    for mes in range(1, meses + 1):
        total +=  ahorro_mensual
        print(f"Mes {mes}: ahorro acumulado = {total} pesos")
    if tota >= meta:
        print("¡Felicidades! Has alcanzado tu meta de ahorro.")
    else:
        print(f"Aún te faltan {meta - total} pesos para alcanzar tu meta de ahorro.")
        