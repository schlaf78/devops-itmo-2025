

Product = ['Orange', 'Banana', 'Lemon']
ProductCost =  [100, 200, 300]
ProductCashierCode = [666, 999, 123]

Receipe = list(zip(Product, ProductCost, ProductCashierCode))
for Item in Receipe:
    print(Item)