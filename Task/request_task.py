import requests

url = "https://fakestoreapi.com/products"

req = requests.get(url)

data = req.json()

total = 0

for i in data :
    print(f"Title : {i['title']}")
    print(f"Price : {i['price']}")
    print(f"Image : {i['image']}")
    print()

    total += i['price']

print(f"Total price : {total}")