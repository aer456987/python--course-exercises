#記帳程式4
products = []
while True:
    name = input('輸入商品名稱: ')
    if name == 'q':
        break
    price = input('輸入價格: ')
    products.append([name,price])
print(products)

for p in products:
    print(p)

with open('text.txt', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

with open('text.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')