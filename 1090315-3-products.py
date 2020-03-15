#記帳程式1
products = []
while True:
    name = input('輸入商品名稱: ')
    if name == 'q':
        break
    price = input('輸入價格: ')
    p = []
    p.append(name)
    p.append(price)
    products.append(p)
print(products)
for product in products:
    print(product)