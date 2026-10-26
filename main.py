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

def procesar_carritos(carritos):
    resultados = []

    for cart in carritos:
        cart_id = cart.get("id")
        user_id = cart.get("userId")
        cantidad_validos = 0
        suma_monto_valido = 0

        for product in cart.get("products", []):
            discount_percentage = product.get("discountPercentage", 0)

            if discount_percentage < 12.0:
                quantity = product.get("quantity", 0)
                price = product.get("price", 0)

                cantidad_validos += quantity
                suma_monto_valido += quantity * price

        resultados.append({
            "cart_id": cart_id,
            "user_id": user_id,
            "cantidad_validos": cantidad_validos,
            "monto_valido": round(suma_monto_valido, 2)
        })

    return resultados