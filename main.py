import requests
url = "https://dummyjson.com/carts"
response = requests.get(url)

if response.status_code == 200:
    data_carts = response.json()
    carts = data_carts.get("carts", [])
    print(f"Éxito: Se obtuvieron {len(carts)} carritos.")
    print(carts)
else:
    print(f"Error al obtener los carritos: {response.status_code}")
    carts = []
LIMITE_DESCUENTO = 12


def calcular_productos_validos(carritos):
    resultados = []

    for carrito in carritos:
        cantidad_validos = 0

        for producto in carrito["products"]:
            if producto["discountPercentage"] < LIMITE_DESCUENTO:
                cantidad_validos += producto["quantity"]

        resultados.append({
            "user_id": carrito["userId"],
            "cantidad_validos": cantidad_validos,
        })

    return resultados

lista_resultados = calcular_productos_validos(carts)

print("--- RESULTADOS DE PRODUCTOS VÁLIDOS POR CARRITO ---")
for r in lista_resultados:
    print(f"User ID: {r['user_id']} | Cantidad de productos válidos: {r['cantidad_validos']}")