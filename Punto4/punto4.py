Banco = [100, 200, 300]
total = sum(Banco)
meta = 1000

if total >= meta:
    print("¡Felicidades! Has alcanzado tu meta de ahorro.")
else:
    falta = meta - total
    print(f"Aún te faltan {falta} pesos para alcanzar tu meta de ahorro.")  