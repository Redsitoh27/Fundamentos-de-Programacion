def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento aplicando el porcentaje al monto total
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada 1: solo se proporciona el monto total (usa el descuento predeterminado del 10%)
monto1 = 200
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"Llamada 1: Monto total: ${monto1:.2f}, Descuento: ${descuento1:.2f}, Monto final: ${monto_final1:.2f}")

# Llamada 2: se proporciona el monto total y un porcentaje de descuento del 15%
monto2 = 350
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
monto_final2 = monto2 - descuento2
print(f"Llamada 2: Monto total: ${monto2:.2f}, Descuento: ${descuento2:.2f}, Monto final: ${monto_final2:.2f}")