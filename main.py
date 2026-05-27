#Nombre: Jose Luis Moreno
#Grupo: 213022_297
#Programa: Ingeniería de Sistemas
#Código Fuente: autoría propia
#Problema 3

#definir la lista que contiene el menú
menu = [
    ["Churrasco","Carnes",40000],
    ["Carne al horno","Carnes",30000],
    ["Pizza Colombiana","Pizza",30000],
    ["Pizza Pollo Hawaiana BBQ","Pizza",28000],
    ["Lasaña Boloñesa","Pasta",22000],
    ["Lasaña Mixta","Pasta",27000],
    ["Hamburguesa mixta","Fast Food",28000],
    ["Hamburguesa doble carne","Fast Food",30000],
    ["Cheesecake","Postre",15000],
    ["Postre de Frutas","Postre",13000],
]

# Parámetros de descuento
categoria_descuento = "Pasta"
umbral_precio = 23000   # solo productos de pasta con precio base > 23000 reciben el descuento

# módulo de calculo
def calcular_precio_final(producto, categoria_descuento, umbral):
    nombre, categoria, precio_base = producto
    if categoria == categoria_descuento and precio_base > umbral:
        return round(precio_base * 0.85, 2)
    return precio_base

print(f"{'Producto':<25} {'Categoría':<10} {'Precio Base':>12} {'Precio Final':>13} {'% Descuento':>10}")
print("-" * 80)

for producto in menu:
    nombre, categoria, precio_base = producto
    precio_final = calcular_precio_final(producto, categoria_descuento, umbral_precio)
    #operador ternario para mostrar el descuento aplicado
    descuento = "" if precio_final == precio_base else "15%"
    print(f"{nombre:<25} {categoria:<10} ${precio_base:>10,} ${precio_final:>11,.2f}  {descuento:>8}")