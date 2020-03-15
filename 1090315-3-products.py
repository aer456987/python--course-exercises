#記帳程式1
products = []
while True:
    name = input('輸入商品名稱: ')
    if name == 'q':
        break
    price = input('輸入價格: ')
    products.append(name)
    products.append(price)

print(products)
for product in products:
    print(product)