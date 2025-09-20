# CalculoDescuentoPython.py
# Autor: Gabriela Yepez
# Descripción: Programa para calcular descuento en compras usando funciones en Python.

# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento basado en el monto total de la compra.
    :param monto_total: float -> monto total de la compra
    :param porcentaje_descuento: float -> porcentaje de descuento (por defecto 10%)
    :return: float -> monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
def main():
    # Primer caso: usando el descuento por defecto (10%)
    compra1 = 150.0  # monto de la primera compra
    descuento1 = calcular_descuento(compra1)
    monto_final1 = compra1 - descuento1
    print(f"Compra 1: Monto = ${compra1}, Descuento = ${descuento1}, Total a pagar = ${monto_final1}")

    # Segundo caso: usando un descuento personalizado (por ejemplo, 20%)
    compra2 = 250.0  # monto de la segunda compra
    descuento2 = calcular_descuento(compra2, 20)
    monto_final2 = compra2 - descuento2
    print(f"Compra 2: Monto = ${compra2}, Descuento = ${descuento2}, Total a pagar = ${monto_final2}")


# Llamada a la función principal
if __name__ == "__main__":
    main()
