products = [ 
    {"name": "Keyboard", "price": 45}, 
    {"name": "Monitor", "price": 180}, 
    {"name": "Mouse", "price": 25}, 
    {"name": "Headphones", "price": 75}, 
    {"name": "USB Drive", "price": 15}, 
    {"name": "Webcam", "price": 60} 
]

cheap_products = list(filter(lambda cost: cost["price"] < 50, products))
print("Products under $50:")
for item in cheap_products:
    print(item)