# [編碼練習三(function運用)]-商品計數

data = ['牛肉麵 120', '酸辣湯 30', '火腿蛋餅 35', '牛肉麵 70', '水果茶 65']

def food(data):
    foods = {}
    for f in data:
        name, price= f.split(' ')
        price = int(price)    # 轉換成數字
        if name in foods:
            foods[name] += price  # 如果名字重複，就相加
        else:
            foods[name] = price
    print(foods)
    return foods
food(data)