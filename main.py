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


if lista_resultados:
    ganador = max(lista_resultados, key=lambda r: r["cantidad_validos"])

    url_usuario = f"https://dummyjson.com/users/{ganador['user_id']}"
    response_usuario = requests.get(url_usuario)

    if response_usuario.status_code == 200:
        usuario = response_usuario.json()

        print("\n--- CLIENTE CON MÁS PRODUCTOS VÁLIDOS ---")
        print(f"User ID: {ganador['user_id']}")
        print(f"Cantidad de productos válidos: {ganador['cantidad_validos']}")
    else:
        print(f"Error al obtener el usuario: {response_usuario.status_code}")
else:
    print("No hay resultados para analizar.")