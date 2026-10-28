def calculate_bill(prices,tax_rate=0.10,discount=0.20):
    subtotal=sum(prices)
    d=subtotal*discount
    tax=(subtotal-d)*tax_rate
    total=subtotal-d+tax
    print("Subtotal:",format(subtotal,".2f"))
    print("Discount:",format(d,".2f"))
    print("Tax:",format(tax,".2f"))
    print("Final total:",format(total,".2f"))
prices=[100,50]
calculate_bill(prices,tax_rate=0.10,discount=0.20)