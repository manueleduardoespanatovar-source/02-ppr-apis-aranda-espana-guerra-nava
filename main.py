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

