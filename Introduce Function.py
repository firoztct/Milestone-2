# Introduce Function

#Practice 1

def mobile_price(usd_price,exchange_rate):
    bd_price = usd_price * exchange_rate
    return bd_price

Huawei_Price = mobile_price (230, 100)

print(Huawei_Price)

#Practice 2

def laptop_price_bd (usd_price, bd_price):
    bd_price = usd_price * bd_price
    return bd_price

Huawei_Laptop = laptop_price_bd(450, 100)
print(Huawei_Laptop)

#Practice 3

def currancy_calculate (usd, bd):
    bd_rate = usd * bd
    return bd_rate
Today_rate = currancy_calculate(500, 99)
print(Today_rate)